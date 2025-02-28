# PDF PROFESSOR 1.0

## Overview

**PDF Professor 1.0** extracts text from PDFs using **PyMuPDF** (with a **Poppler** fallback), then processes the text in chunks through an Ollama model using a user-defined prompt. This makes it ideal for summarization, data extraction, and text analysis.

### Key Features:
- **Text Extraction & Chunking** – Efficiently processes large PDFs into manageable sections.
- **Custom Prompt Processing** – Guides the Ollama model dynamically with your input.
- **Logging & Resume Support** – Tracks progress to continue where it left off.
- **Timeout & Concurrency Control** – Optimizes performance by adjusting processing limits.

---
## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/PDF-Professor.git
cd PDF-Professor
```

### 2. Set Up Environment
```bash
conda create -n pdfprofessorENV python=3.10
conda activate pdfprofessorENV
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---
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

---
## Usage

### 1. Run the Program
```bash
python pdfprofessor.py
```

### 2. Enter Your Prompt
```
Enter your prompt for Ollama: Summarize key points.
```

### 3. Processing & Output
- Chunks PDFs and processes them via Ollama.
- Saves processed content in `ProcessedChunks` and combined scripts in `Scripts`.

---
## Model Selection & Setup

### Recommended Models:
- **WizardLM 2:7B** – Primary model optimized for deep text analysis.
- **DeepSeek-R1:7B** – Ideal for case law reasoning and cybersecurity reports.
- **Mistral or LLaMA 3.1** – Best for speed-focused processing of large PDF batches.

### Changing Models:
1. **Modify `config.json`**
   - Locate the `ollama_command` setting and change the model name. Example:
   
   ```json
   "ollama_command": ["ollama", "run", "deepseek-r1:7b"]
   ```

2. **Ensure the Model is Downloaded Locally**
   ```bash
   ollama pull <model-name>
   ```
   Example:
   ```bash
   ollama pull deepseek-r1:7b
   ```

3. **Verify Available Models**
   ```bash
   ollama list
   ```

4. **Test Model Performance**
   ```bash
   ollama run <model-name>
   ```
   Example:
   ```bash
   ollama run mistral:latest
   ```

Once the model is set in `config.json`, **restart** PDF Professor to apply the changes.

---
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

---
## Prompt List

### OSINT & Investigations
#### Fraud & Financial Crimes:
- Identify and analyze patterns in fraud schemes, financial crimes, and risk assessment methodologies.
- Detect and analyze trends in whistleblower disclosures related to fraud and misconduct.
- Convert whistleblower testimonies or case disclosures into structured datasets for fraud detection and AI-assisted risk analysis.
- Parse and analyze financial records, including bank statements and transaction histories, to detect anomalies and fraudulent activities.
- Examine corporate and government financial reports to identify trends, discrepancies, and regulatory compliance issues.

#### Social Media & Misinformation:
- Analyze patterns in social media misinformation campaigns and their impact.
- Extract social media investigation techniques and categorize them by platform, methodology, and risk factors.
- Identify and categorize social media manipulation tactics used in misinformation campaigns.
- Identify references to AI-generated misinformation and structure them into datasets for detection and mitigation training.

#### Surveillance & Intelligence Gathering:
- Identify and categorize surveillance techniques used in corporate and law enforcement settings, including digital vs. physical methodologies.
- Extract intelligence-gathering methodologies applicable to business investigations and OSINT.
- Identify intelligence-gathering techniques used in OSINT investigations and legal contexts.
- Categorize intelligence cycle references into collection, analysis, dissemination, and operational use.

#### Case Studies & Incident Analysis:
- Analyze crash reports to identify contributing factors, patterns, and potential liabilities.
- Review and summarize incident reports to highlight key events, responsible parties, and procedural gaps.
- Extract relevant statements from witness testimonies and analyze inconsistencies for case evaluation.
- Parse case studies of past cyberattacks and summarize them as structured incident reports.
- Identify trends and patterns in criminal behavior based on case study data.
- Extract real-world OSINT case studies and format them for AI-assisted investigation workflows.

### Legal
#### Legal Analysis & Case Law:
- Extract and structure legal statutes, case laws, and precedents for AI-driven legal analysis.
- Identify and analyze patterns in legal case outcomes to predict case trajectories.
- Analyze historical patterns in legal cases to determine causation and liability, identifying contributing factors and responsible parties.

#### Witness & Evidence Analysis:
- Identify recurring themes and inconsistencies in witness statements to assess reliability.
- Examine, analyze, and detail inconsistencies in depositions and court transcripts.
- List witnesses and categorize their statements based on relevance and reliability.
- Organize legal evidence and testimonies for structured case-building.

#### Regulatory & Compliance:
- Extract all legal definitions, jurisdictional laws, and regulatory frameworks for different types of cybercrime.
- Identify all data privacy laws and format them as structured training sets for compliance analysis.
- Summarize all regulations on electronic surveillance and data retention laws across different jurisdictions.

### Cybersecurity
#### Threat Analysis & Incident Response:
- Analyze patterns in cybersecurity incidents, including intrusion attempts and attack methodologies.
- Analyze threat actors involved in ransomware and breach data attacks.
- Parse the document for mentions of threat actors, hacking groups, or cybercriminal organizations and summarize their activities.
- Summarize all incident response frameworks and standard operating procedures for AI-assisted cybersecurity training.

#### Attack Vectors & Defenses:
- Generate a structured list of attack vectors, defenses, and mitigation strategies.
- Convert hacking methodologies and defense mechanisms into red team vs. blue team training sets.
- Identify cybersecurity frameworks like NIST, ISO 27001, and CIS controls and format them into structured datasets.

#### Insider Threats & Counterintelligence:
- Extract and categorize all references to insider threats and mitigation strategies.
- Extract all discussions on counterintelligence tactics and cyber deception strategies.

#### Phishing & Misinformation:
- Identify structured datasets related to phishing techniques and misinformation campaigns.
- Extract structured datasets on phishing techniques, categorized by attack type and mitigation strategies.

---
## Troubleshooting

- **Timeout Errors** – Increase timeout settings.
- **Slow Performance** – Reduce chunk size or adjust concurrency.
- **Model Choice** – Use a smaller Ollama model if needed.

---
## License

This project is available under the [MIT License](LICENSE). Contributions are welcome!

