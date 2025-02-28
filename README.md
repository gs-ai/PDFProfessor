```markdown
<!-- 
   NOTE: GitHub Flavored Markdown does not natively support custom colors or neon outlines.
   The ASCII-style boxes and headings below are designed for a more "visual" layout
   without using images, icons, or animated GIFs.
-->

# ┌─────────────────────────────────────────────────────────────────────────┐
# │                         PDF PROFESSOR 1.0                             │
# └─────────────────────────────────────────────────────────────────────────┘

**A streamlined pipeline for extracting and processing PDF content, then training an Ollama model on text chunks, all guided by a user-defined prompt.**

---

## ╔══ OVERVIEW ═════════════════════════════════════════════════════════╗
PDF Professor 1.0 extracts text from PDFs using PyMuPDF (with a Poppler fallback), breaks the text into **manageable chunks**, and processes each chunk via an Ollama command.

- **Chunking & Logging**: Splits large documents and keeps track of your progress.
- **Custom Prompt**: You can specify exactly what you want Ollama to do with each chunk.
- **Timeout & Concurrency Control**: Designed to minimize processing delays and resource overload.

```plaintext
   ┌────────────────────────────┐
   │   PDF FILE(S)  ----->     │
   │  (Input Directory)        │
   └────────────────────────────┘
                ↓
      [ PDF Professor 1.0 ]
                ↓
   ┌────────────────────────────┐
   │   Processed Chunks        │
   │  (Output Directory)       │
   └────────────────────────────┘
                ↓
       [ Model Training ]
```

---

## ╔══ CONFIGURATION ════════════════════════════════════════════════════╗

All settings live in `config.json`. Example:

```json
{
    "pdf_directory": "PDF",
    "output_directory": "Scripts",
    "log_directory": "Logs",
    "chunk_storage_directory": "ProcessedChunks",
    "ollama_command": ["ollama", "run", "wizardlm2:7b"],
    "chunk_size": 2000
}
```

- **pdf_directory**: Where your input PDFs are located  
- **output_directory**: Where the final processed scripts are stored  
- **log_directory**: For progress and error logs  
- **chunk_storage_directory**: Where individual chunk files go  
- **ollama_command**: Command + arguments to run your chosen Ollama model  
- **chunk_size**: Number of characters per chunk

---

## ╔══ INSTALLATION ═════════════════════════════════════════════════════╗

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YourUsername/PDF-Professor.git
   cd PDF-Professor
   ```

2. **Set Up Environment**  
   ```bash
   conda create -n pdfprofessorENV python=3.10
   conda activate pdfprofessorENV
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## ╔══ USAGE ════════════════════════════════════════════════════════════╗

1. **Run the Main Script**  
   ```bash
   python pdfprofessor.py
   ```
2. **Enter Your Prompt** (no quotes needed) when asked:
   ```
   Enter your prompt for Ollama: Extract headings and summarize each section.
   ```
3. **Processing**  
   - The script will process each PDF in your `pdf_directory`, splitting it into chunks.  
   - Each chunk is sent to the Ollama model with your custom prompt.  
   - Processed chunks are saved in `ProcessedChunks`.  
   - A final combined script is saved in `Scripts`.  
   - The model is then trained on the combined output.

---

## ╔══ FILE STRUCTURE ═══════════════════════════════════════════════════╗

```plaintext
PDF-Professor/
├── pdfprofessor.py              # Main script
├── config.json                  # Configuration file
├── requirements.txt             # Dependencies
├── PDF/                         # Place your PDF files here
├── Logs/                        # Log files stored here
├── ProcessedChunks/             # Individual chunk outputs
└── Scripts/                     # Final processed scripts
```

---

## ╔══ KEY FEATURES ═════════════════════════════════════════════════════╗

- **Flexible Prompt Input**: Quickly adapt the pipeline to summarization, extraction, or any other text manipulation.  
- **Timeout & Concurrency Controls**: Prevent model overload by limiting the number of threads and increasing timeouts as needed.  
- **Resume Support**: If you interrupt the process, it picks up from the last processed chunk.  
- **Fallback PDF Parsing**: If PyMuPDF fails, the script automatically uses Poppler (`pdftotext`).

---

## ╔══ TROUBLESHOOTING & TIPS ═══════════════════════════════════════════╗

- **Timeouts**: If you see repeated timeout errors, increase `timeout` in `process_with_ollama` and `train_ollama_model`.  
- **Concurrency**: Lower `max_workers` if your system is resource-constrained.  
- **Chunk Size**: Decrease `chunk_size` if the text is too large or the model is slow.  
- **Model Choice**: Try smaller or more optimized Ollama models if performance lags.

---

## ╔══ LICENSE ══════════════════════════════════════════════════════════╗

This project is available under the [MIT License](LICENSE). Contributions are welcome!

---

**PDF Professor 1.0** – *Because your PDFs deserve a well-trained mind.*  
```
