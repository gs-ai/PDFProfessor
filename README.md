# PDF PROFESSOR 1.0

## Overview

**PDF Professor 1.0** extracts text from PDFs using **PyMuPDF** (with a **Poppler** fallback), then processes the text in chunks through an Ollama model using a user-defined prompt. This makes it ideal for summarization, data extraction, and text analysis.

### Key Features:
- **Text Extraction & Chunking** – Efficiently processes large PDFs into manageable sections.
- **Custom Prompt Processing** – Guides the Ollama model dynamically with your input.
- **Logging & Resume Support** – Tracks progress to continue where it left off.
- **Timeout & Concurrency Control** – Optimizes performance by adjusting processing limits.

## Configuration

All settings are stored in `config.json`:

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

| Key                         | Description                                     |
|-----------------------------|-------------------------------------------------|
| **pdf_directory**           | Folder containing PDF files                     |
| **output_directory**        | Where processed scripts are saved               |
| **log_directory**           | Logs progress and errors                        |
| **chunk_storage_directory** | Stores individual chunk outputs                 |
| **ollama_command**          | Defines how Ollama runs                         |
| **chunk_size**              | Number of characters per chunk                  |

## Installation

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

## Usage

1. **Run the Program**
   ```bash
   python pdfprofessor.py
   ```
2. **Enter Your Prompt**
   ```
   Enter your prompt for Ollama: Summarize key points.
   ```
3. **Processing & Output**
   - Chunks PDFs and processes them via Ollama.
   - Saves processed content in `ProcessedChunks` and combined scripts in `Scripts`.

## File Structure

```plaintext
PDF-Professor/
├── pdfprofessor.py              # Main script
├── config.json                  # Configuration file
├── requirements.txt             # Dependencies
├── PDF/                         # Source PDFs
├── Logs/                        # Logs
├── ProcessedChunks/             # Chunk outputs
└── Scripts/                     # Final scripts
```

## Troubleshooting

- **Timeout Errors** – Increase timeout settings.
- **Slow Performance** – Reduce chunk size or adjust concurrency.
- **Model Choice** – Use a smaller Ollama model if needed.

## License

This project is available under the [MIT License](LICENSE). Contributions are welcome!

