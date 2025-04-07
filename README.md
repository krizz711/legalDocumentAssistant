🧾 Legal Document Assistant (Contract Analyzer)
This Streamlit-based web app helps analyze legal contracts by:

📄 Summarizing the document with key sections like obligations, payment terms, and termination clauses

⚠️ Detecting risky clauses such as indemnity, penalties, and limitation of liability

❓ Answering questions about the contract using vector search and Gemini Pro (via LangChain)

Built using:

Streamlit, LangChain, FAISS, Gemini Pro, and PyPDF2

Google Generative AI for embeddings and legal understanding

Upload a PDF, and get smart legal insights in seconds!

Let me know if you'd like a longer README with setup instructions too.







You said:
shart description for reposatery creation


ChatGPT said:
Here's a short and concise description for your repository creation:

"A Streamlit app that summarizes legal contracts, detects risky clauses, and answers legal questions using Gemini Pro and vector search."

Let me know if you want a one-liner tagline or tags too.







You said:
write a read me filr for it


ChatGPT said:
Here’s a complete README.md file for your Legal Document Assistant repository:

# 🧾 Legal Document Assistant (Contract Analyzer)

A Streamlit-based application that helps users analyze legal contracts by summarizing key sections, identifying risky clauses, and answering questions using Google's Gemini Pro and vector search (FAISS).

---

## ✨ Features

- 📄 **Document Summary**  
  Get a concise summary of the uploaded legal contract highlighting key sections like:
  - Obligations
  - Payment Terms
  - Term & Termination
  - Confidentiality
  - Penalties

- ⚠️ **Risky Clause Detection**  
  Automatically identify sensitive or risky clauses related to:
  - Termination
  - Indemnity
  - Confidentiality
  - Penalties
  - Limitation of Liability

- ❓ **Contract Q&A**  
  Ask questions in plain English, and get context-based legal answers using:
  - Google Generative AI Embeddings
  - LangChain
  - FAISS Vector Search

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI & interaction
- [LangChain](https://www.langchain.com/) – LLM orchestration
- [Gemini Pro](https://ai.google.dev/) – Question answering & summarization
- [FAISS](https://github.com/facebookresearch/faiss) – Vector similarity search
- [PyPDF2](https://pypi.org/project/PyPDF2/) – PDF text extraction

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/legal-document-assistant.git
cd legal-document-assistant
2. Install Dependencies
pip install -r requirements.txt
3. Set Up Environment Variables
Create a .env file in the root directory and add:

GOOGLE_API_KEY=your_google_api_key
Also, set the path to your Google service account key (for Gemini) in your script or environment:

python

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account.json"
4. Run the App

streamlit run app.py
 
📌 Example Use Case
Upload a legal contract PDF.

View a clean summary of the contract.

Identify clauses that may be legally risky.

Ask questions like:

"What are the termination conditions?"

"Who is responsible for payment?"

🧠 Powered By
🧠 Google Gemini Pro (via LangChain)

🔍 FAISS Vector Store

🧾 PyPDF2 for document parsing

📜 License
MIT License. See LICENSE for more details.

🙌 Contributions
Contributions are welcome! Feel free to fork, improve, or suggest enhancements.

