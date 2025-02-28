'''markdown
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                       PDF PROFESSOR 1.0                       ┃
# ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
# ┃ A robust pipeline for extracting PDF content, chunking text,  ┃
# ┃ and training an Ollama model using your custom prompt.        ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

---
'''

## ━━ OVERVIEW ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**PDF Professor 1.0** extracts text from PDFs using **PyMuPDF** (with a **Poppler** fallback), then breaks the text into manageable chunks. Each chunk is processed by an Ollama model command, **guided by your prompt** at runtime—ideal for summarizing, extracting insights, or any specialized text manipulation.

Key highlights:

- **Chunking & Logging**  
  Splits large documents into smaller pieces and logs progress for easy resumption.  
- **Custom Prompt**  
  Dynamically control how each chunk is processed by the Ollama model.  
- **Timeout & Concurrency**  
  Prevent overload by tuning the number of threads and the processing timeout.

---

## ━━ CONFIGURATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

All settings are stored in `config.json`. Example:

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

| Key                         | Description                                             |
|-----------------------------|---------------------------------------------------------|
| **pdf_directory**           | Folder containing your PDF files                       |
| **output_directory**        | Where combined processed scripts will be saved         |
| **log_directory**           | Stores logs for progress and errors                    |
| **chunk_storage_directory** | Directory for individual chunk outputs                 |
| **ollama_command**          | Command & arguments to run your Ollama model           |
| **chunk_size**              | Characters per chunk before splitting                  |

---

## ━━ INSTALLATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YourUsername/PDF-Professor.git
   cd PDF-Professor
   ```
2. **Set Up a Conda Environment**
   ```bash
   conda create -n pdfprofessorENV python=3.10
   conda activate pdfprofessorENV
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ━━ USAGE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **Run the Program**
   ```bash
   python pdfprofessor.py
   ```
2. **Enter Your Prompt** when prompted (no quotes needed):
   ```
   Enter your prompt for Ollama: Summarize each section and list page numbers.
   ```
3. **Processing & Output**
   - Splits each PDF in `pdf_directory` into smaller text chunks.  
   - Sends each chunk to the Ollama model with your **prompt**.  
   - Saves processed chunks to `ProcessedChunks` and a combined script to `Scripts`.  
   - Trains the Ollama model on the merged content.

---

## ━━ FILE STRUCTURE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```plaintext
PDF-Professor/
├── pdfprofessor.py              # Main script
├── config.json                  # Configuration file
├── requirements.txt             # Dependencies
├── PDF/                         # Source PDFs
├── Logs/                        # Logs (progress, errors)
├── ProcessedChunks/             # Individual chunk outputs
└── Scripts/                     # Final processed scripts
```

---

## ━━ KEY FEATURES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- **Flexible Prompt Input**  
  Instantly shift tasks: summarization, data extraction, Q&A, etc.  
- **Timeout & Concurrency Control**  
  Adjust thread usage (`max_workers`) and timeouts to prevent slowdowns.  
- **Resume Support**  
  Picks up where it left off if the process is interrupted.  
- **Fallback PDF Parsing**  
  Automatically switches to `pdftotext` if PyMuPDF fails.

---

## ━━ TROUBLESHOOTING ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- **Timeout Errors**  
  Increase `timeout` in both `process_with_ollama` and `train_ollama_model`.  
- **Slow Performance**  
  Use smaller chunks (e.g., 500–1000 chars) or reduce concurrency.  
- **Model Choice**  
  If `wizardlm2:7b` is too heavy, consider a smaller Ollama model.

---

## ━━ LICENSE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This project is available under the [MIT License](LICENSE). Contributions are welcome!

---

**PDF Professor 1.0** – *Streamlined PDF text processing with the power of your prompt.*  
