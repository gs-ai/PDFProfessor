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

# PROMPT LIST

## Investigations
- Extract legal statutes, case laws, and relevant precedents and format them for structured AI training.
- Identify and summarize discussions on fraud schemes, including case studies for AI learning.
- Convert whistleblower testimonies or case disclosures into structured datasets for AI-assisted risk analysis.
- Extract surveillance techniques and categorize them based on digital vs. physical methodologies.
- Identify intelligence-gathering techniques used in OSINT investigations.
- Parse case studies of past cyberattacks and summarize them as structured incident reports.
- Extract forensic analysis procedures and structure them as a step-by-step guide.
- Summarize risk assessment methodologies and classify them based on cybersecurity, physical security, and fraud prevention.
- Identify trends and patterns in criminal behavior based on case study data.
- Extract real-world OSINT case studies and format them for AI-assisted investigation workflows.
- Identify past cyber espionage campaigns and summarize key takeaways for AI-assisted counterintelligence training.
- Extract discussions on nation-state cyber warfare strategies and summarize key threat intelligence findings.
- Parse geopolitical intelligence reports and extract structured indicators for AI-assisted situational awareness.

## Cybersecurity
- Parse the document for mentions of threat actors, hacking groups, or cybercriminal organizations and summarize their activities.
- Extract all discussions on counterintelligence tactics and cyber deception strategies.
- Generate a structured list of attack vectors, defenses, and mitigation strategies.
- Identify all digital evidence handling procedures and convert them into best practices for forensic AI training.
- Summarize all incident response frameworks and standard operating procedures for AI-assisted cybersecurity training.
- Parse cybersecurity reports and extract key statistics, trends, and predictions for structured training.
- Convert hacking methodologies and defense mechanisms into red team vs. blue team training sets.
- Identify cybersecurity frameworks like NIST, ISO 27001, and CIS controls and format them into structured datasets.
- Extract and categorize all references to insider threats and mitigation strategies.
- Extract deepfake detection methodologies and structure them into training data for AI-assisted fraud prevention.
- Parse classified document leak case studies and summarize legal, ethical, and investigative responses.

## OSINT
- Extract social media investigation techniques and categorize them based on platform, methodology, and risk factors.
- List OSINT techniques and methodologies and categorize them based on use cases.
- Extract structured datasets on phishing techniques, categorized by attack type and mitigation strategies.
- Identify and categorize social media manipulation tactics used in misinformation campaigns.
- Identify all intelligence cycle references and categorize them into collection, analysis, dissemination, and operational use.
- Identify social network analysis methodologies used for tracking threat actors.
- Extract structured data on OSINT tools, their use cases, and operational risks.
- Identify all references to AI-generated misinformation and structure them into datasets for detection and mitigation training.
- Extract references to surveillance law, wiretapping regulations, and data monitoring policies.
- Parse cybersecurity frameworks and extract data relevant to open-source intelligence gathering.

## Legal
- Extract legal arguments used in past court cases and format them into structured training examples.
- Identify and summarize all discussions on legal challenges in ethical hacking and penetration testing.
- Extract references to surveillance law, wiretapping regulations, and data monitoring policies.
- Extract and structure intelligence-gathering techniques used in legal investigations.
- Extract all legal definitions, jurisdictional laws, and regulatory frameworks for different types of cybercrime.
- Identify all data privacy laws and format them as structured training sets for compliance analysis.
- Summarize all regulations on electronic surveillance and data retention laws across different jurisdictions.
- Identify legal challenges and case law related to ethical hacking and penetration testing.
- Extract detailed information on law enforcement techniques for tracking digital assets and cryptocurrency transactions.
- Parse legal case studies involving digital evidence and summarize chain of custody best practices.

## Troubleshooting

- **Timeout Errors** – Increase timeout settings.
- **Slow Performance** – Reduce chunk size or adjust concurrency.
- **Model Choice** – Use a smaller Ollama model if needed.

## License

This project is available under the [MIT License](LICENSE). Contributions are welcome!

