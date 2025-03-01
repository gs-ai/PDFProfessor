import os
import fitz  # PyMuPDF
import subprocess
import concurrent.futures
import logging
import json
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration from a JSON file
def load_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        return json.load(f)

config = load_config()

pdf_directory = config['pdf_directory']
output_directory = config['output_directory']  # Or a fixed path if you prefer
log_directory = config['log_directory']
chunk_storage_directory = config['chunk_storage_directory']
ollama_command = config['ollama_command']
chunk_size = config['chunk_size']
progress_log_file = os.path.join(log_directory, 'progress.log')
scripts_directory = "/Users/mbaosint/Desktop/Projects/PDF-Professor/Scripts"

# Create directories if they do not exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(log_directory, exist_ok=True)
os.makedirs(chunk_storage_directory, exist_ok=True)
os.makedirs(scripts_directory, exist_ok=True)

# Function to load progress log
def load_progress_log():
    if os.path.exists(progress_log_file):
        with open(progress_log_file, 'r') as f:
            return json.load(f)
    return {}

# Function to update progress log
def update_progress_log(file_name, chunk_index):
    progress_log[file_name] = chunk_index
    with open(progress_log_file, 'w') as f:
        json.dump(progress_log, f)

# Function to process text with Ollama
def process_with_ollama(text_chunk, user_prompt):
    combined_prompt = f"{user_prompt}\n\n{text_chunk}"
    try:
        process = subprocess.Popen(
            ollama_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=combined_prompt, timeout=120)
        if process.returncode != 0:
            logging.error(f"Ollama processing failed: {stderr}")
            return text_chunk
        return stdout
    except subprocess.TimeoutExpired:
        logging.error("Ollama processing timed out!")
        return text_chunk
    except Exception as e:
        logging.error(f"Error in process_with_ollama: {e}")
        return text_chunk

# Function to train the Ollama model
def train_ollama_model(text):
    try:
        process = subprocess.Popen(
            ollama_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=text, timeout=120)
        if process.returncode != 0:
            logging.error(f"Ollama training failed: {stderr}")
            return stderr
        return stdout
    except subprocess.TimeoutExpired:
        logging.error("Ollama training timed out!")
        return "Training timeout"
    except Exception as e:
        logging.error(f"Error in train_ollama_model: {e}")
        return str(e)

# Function to save processed data locally
def save_data_locally(file_name, data, directory):
    file_path = os.path.join(directory, file_name)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        return file_path
    except Exception as e:
        logging.error(f"Error saving data locally: {e}")
        return None

# Function to read PDF files
def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        content = ''
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            content += page.get_text()
        return content
    except Exception as e:
        logging.warning(f"PyMuPDF failed to read {file_path}, falling back to poppler: {e}")
        try:
            from subprocess import run
            text = run(["pdftotext", file_path, "-"], capture_output=True, text=True).stdout
            return text
        except Exception as e:
            logging.error(f"Poppler also failed to read {file_path}: {e}")
            return None

def process_file(file_name, user_prompt):
    try:
        file_path = os.path.join(pdf_directory, file_name)
        content = read_pdf(file_path)
        if content:
            chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
            processed_content = ''
            last_processed_chunk = progress_log.get(file_name, 0)
            
            with tqdm(total=len(chunks), desc=f'Processing {file_name}', dynamic_ncols=True) as pbar:
                with ThreadPoolExecutor(max_workers=1) as executor:
                    future_chunks = {
                        executor.submit(process_with_ollama, chunk, user_prompt): i
                        for i, chunk in enumerate(chunks)
                        if i >= last_processed_chunk
                    }
                    for future in as_completed(future_chunks):
                        processed_chunk = future.result()
                        chunk_index = future_chunks[future]
                        processed_content += processed_chunk
                        update_progress_log(file_name, chunk_index + 1)
                        pbar.update(1)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            script_name = f"script_{timestamp}.txt"
            save_data_locally(script_name, processed_content, scripts_directory)
            
            train_output = train_ollama_model(processed_content)
            logging.info(f"Processed {file_name}, trained: {train_output}")
            return f"Processed {file_name}, trained: {train_output}"
        else:
            logging.error(f"Failed to read file: {file_name}")
            return f"Failed to read file: {file_name}"
    except Exception as e:
        logging.error(f"Error processing file {file_name}: {e}")
        return f"Error processing file {file_name}: {e}"

def main():
    global progress_log
    progress_log = load_progress_log()
    user_prompt = input("Enter your prompt for Ollama: ")
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(process_file, file_name, user_prompt): file_name for file_name in pdf_files}
        for future in tqdm(as_completed(futures), total=len(futures), desc='Processing PDFs'):
            logging.info(future.result())

if __name__ == "__main__":
    main()
