# ╔══════════════════════════════════════╗
# ║         PDF PROFESSOR 1.0            ║
# ╚══════════════════════════════════════╝
#
# A sleek, robust pipeline for processing PDFs and training on text chunks
# using a customizable prompt with the Ollama model.
#
# ───────────────────────────────────────────────
#
# ## OVERVIEW
#
# This tool extracts text from PDFs, splits the text into manageable chunks,
# and processes each chunk using an Ollama model command. The program:
#
# - **Reads PDFs** with PyMuPDF (with a fallback to poppler)
# - **Splits** extracted text into chunks (default size defined in `config.json`)
# - **Processes** each chunk via an external model (Ollama) using a user-defined prompt
# - **Saves** intermediate chunk files and overall processed scripts
# - **Trains** the model on the concatenated, processed text
#
# The system uses progress logging and concurrency (with controlled parallelism)
# to ensure efficient and robust operation.
#
# ───────────────────────────────────────────────
#
# ## FEATURES
#
# ┌──────────────────────────────────────────────┐
# │ • **Custom Prompt:** Specify a task prompt before processing │
# │ • **Timeout Management:** Increased timeout settings to avoid delays  │
# │ • **Controlled Concurrency:** Single-threaded chunk processing per PDF   │
# │ • **Fallback PDF Parsing:** Automatically switches to poppler if needed │
# └──────────────────────────────────────────────┘
#
# ## CONFIGURATION
#
# The program reads settings from a JSON file (`config.json`). An example configuration:
#
# ```json
# {
#     "pdf_directory": "PDF",
#     "output_directory": "Scripts",
#     "log_directory": "Logs",
#     "chunk_storage_directory": "ProcessedChunks",
#     "ollama_command": ["ollama", "run", "wizardlm2:7b"],
#     "chunk_size": 2000
# }
# ```
#
# *Solid tech colors and a thin neon tracer outline guide the flow of data
# from PDFs to processed scripts.*
#
# ───────────────────────────────────────────────
#
# ## INSTALLATION
#
# 1. **Clone the repository:**
#
#    ```bash
#    git clone https://github.com/yourusername/pdfprofessor.git
#    cd pdfprofessor
#    ```
#
# 2. **Create and activate your virtual environment:**
#
#    ```bash
#    conda create -n pdfprofessorENV python=3.10
#    conda activate pdfprofessorENV
#    ```
#
# 3. **Install dependencies:**
#
#    ```bash
#    pip install -r requirements.txt
#    ```
#
# ───────────────────────────────────────────────
#
# ## USAGE
#
# Run the program using:
#
# ```bash
# python pdfprofessor.py
# ```
#
# When prompted, simply enter your desired prompt (no quotes needed). For example:
#
# > Enter your prompt for Ollama: **Extract the key sections and page numbers from the text.**
#
# The program will then:
#
# - Process each PDF found in the configured directory.
# - Save processed chunks and a full processed script in the specified output directories.
# - Log progress and any errors along the way.
#
# ───────────────────────────────────────────────
#
# ## FILE STRUCTURE
#
# ```plaintext
# pdfprofessor/
# ├── config.json            # Configuration settings
# ├── pdfprofessor.py        # Main application script
# ├── requirements.txt       # Python dependencies
# ├── Logs/                  # Log files (auto-created)
# ├── PDF/                   # Source PDFs (place your PDFs here)
# ├── Scripts/               # Final processed script outputs
# └── ProcessedChunks/       # Intermediate chunk outputs
# ```
#
# ───────────────────────────────────────────────
#
# ## TECH STACK
#
# - **Python 3.10+**
# - **PyMuPDF (fitz)** for PDF reading
# - **Subprocess** for external command invocation (Ollama)
# - **tqdm** for progress visualization
# - **ThreadPoolExecutor** for controlled concurrency
#
# ───────────────────────────────────────────────
#
# ## CUSTOMIZATION & EXTENSIBILITY
#
# *The code is modular and easily adaptable to your needs:*
#
# - **Prompt Customization:** Modify the prompt logic in `process_with_ollama()`
# - **Timeout Adjustments:** Change timeout values in both processing and training functions
# - **Concurrency Limits:** Adjust `max_workers` in the ThreadPoolExecutors for tuning performance
#
# ───────────────────────────────────────────────
#
# ## LICENSE
#
# This project is released under the [MIT License](LICENSE).
#
# ───────────────────────────────────────────────
#
# **PDF Professor** - A powerful tool to bring clarity and structure to your PDF data.
#
