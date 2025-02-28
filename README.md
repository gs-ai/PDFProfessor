```markdown
<!-- 
  NOTE: GitHub Flavored Markdown does not allow custom background colors,
  but we can still create a dark, bold, and sleek ASCII-style layout.
  Below is a "manly" look using heavy lines and a thin neon tracer vibe.
-->

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                           PDF PROFESSOR 1.0                          ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

**A streamlined pipeline for extracting and processing PDF content, then training an Ollama model on text chunks—all guided by your custom prompt.**

---

## ╔═════ OVERVIEW ══════════════════════════════════════════════════════╗

**PDF Professor 1.0** extracts text from PDFs using PyMuPDF (with a Poppler fallback), breaks the text into **manageable chunks**, and processes each chunk with an Ollama model command. You supply a **prompt** at runtime, so you can tailor the processing to your exact needs—whether you’re summarizing, extracting key points, or performing advanced text transformations.

```
 ┌─────────────────────────────────────────────────────────┐
 │   PDF FILE(S)  ----->   [ PDF PROFESSOR 1.0 ]   -----> │
 │     (Input)               (Processing)              (Chunks)
 └─────────────────────────────────────────────────────────┘
```

- **Chunking & Logging**: Splits large documents into smaller pieces, keeps track of progress, and resumes if interrupted.  
- **Custom Prompt**: Inject your own instructions for the Ollama model.  
- **Timeout & Concurrency Control**: Prevents your system from overloading.

---

## ╔═════ CONFIGURATION ═════════════════════════════════════════════════╗

All settings live in a `config.json`. Example:

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

| Key                        | Description                                             |
|----------------------------|---------------------------------------------------------|
| **pdf_directory**          | Folder containing your PDF files                       |
| **output_directory**       | Where combined processed scripts will be saved         |
| **log_directory**          | Location of logs for progress and errors               |
| **chunk_storage_directory**| Directory for individual chunk outputs                 |
| **ollama_command**         | The command & arguments to run your Ollama model       |
| **chunk_size**             | Characters per chunk before splitting                  |

---

## ╔═════ INSTALLATION ══════════════════════════════════════════════════╗

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/YourUsername/PDF-Professor.git
   cd PDF-Professor
   ```

2. **Create & Activate Environment**  
   ```bash
   conda create -n pdfprofessorENV python=3.10
   conda activate pdfprofessorENV
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

---

## ╔═════ USAGE ═════════════════════════════════════════════════════════╗

1. **Run the Program**  
   ```bash
   python pdfprofessor.py
   ```
2. **Enter Your Prompt** (no quotes needed) when prompted:
   ```
   Enter your prompt for Ollama: Summarize each section and list page numbers.
   ```
3. **Processing**  
   - Splits each PDF in `pdf_directory` into chunks.  
   - Sends each chunk to Ollama with your prompt.  
   - Saves processed chunks to `ProcessedChunks` and a combined script to `Scripts`.  
   - Trains the model on the combined output.

---

## ╔═════ FILE STRUCTURE ════════════════════════════════════════════════╗

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

## ╔═════ KEY FEATURES ══════════════════════════════════════════════════╗

- **Flexible Prompt Input**: Change tasks on the fly—summaries, Q&A, data extraction, etc.  
- **Timeout & Concurrency**: Adjust timeouts to avoid stalling, limit thread usage for large models.  
- **Resume Support**: If you halt midway, it resumes from the last processed chunk.  
- **Fallback PDF Parsing**: Switches to `pdftotext` if PyMuPDF fails.

---

## ╔═════ TROUBLESHOOTING ═══════════════════════════════════════════════╗

- **Timeout Errors**: Increase the `timeout` value in `process_with_ollama` or `train_ollama_model`.  
- **Model Performance**: If you’re on limited hardware, reduce concurrency (`max_workers`) or use smaller Ollama models.  
- **Chunk Size**: Try smaller chunks (e.g., 500–1000 characters) if processing is too slow.  

---

## ╔═════ LICENSE ═══════════════════════════════════════════════════════╗

This project is available under the [MIT License](LICENSE). Contributions are welcome!

---

**PDF Professor 1.0** – *Where robust PDF processing meets the power of your prompt.*  
```
