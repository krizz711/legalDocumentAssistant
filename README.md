# 🧾 Legal Document Assistant (Contract Analyzer)

A Streamlit-based application that helps users analyze legal contracts by summarizing key sections, identifying risky clauses, and answering questions using Google's Gemini Pro and vector search (FAISS).

---

## ✨ Features

- 📄 **Document Summary** – Highlight obligations, payment terms, termination, confidentiality, and penalties  
- ⚠️ **Risky Clause Detection** – Identify sensitive clauses like indemnity, penalties, and liability  
- ❓ **Contract Q&A** – Ask questions and get accurate responses using vector search & Gemini Pro  

---

![Alt text](C:\Users\Asus\OneDrive\图片\Screenshots\Screenshot 2025-04-06 152132.png)



## 🛠️ Tech Stack

- Streamlit – UI & interaction  
- LangChain – LLM orchestration  
- Gemini Pro – Question answering & summarization  
- FAISS – Vector similarity search  
- PyPDF2 – PDF text extraction  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/legal-document-assistant.git
cd legal-document-assistant
```

### 2. Install dependencies

pip install -r requirements.txt

### 3. Set up environment variables
Create a .env file in the root directory:


GOOGLE_API_KEY=your_google_api_key
In your Python script or terminal, set the service account path:

path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account.json"

### 4. Run the app

streamlit run app.py

## 📌 Example Use Case
Upload a legal contract PDF

View a clean summary

Detect risky clauses

Ask questions like:

"What are the termination conditions?"

"Who is responsible for payment?"

## 🧠 Powered By
Google Gemini Pro (via LangChain)

FAISS Vector Store

PyPDF2

## 📜 License
MIT License. See LICENSE for details.

## 🙌 Contributions
Contributions are welcome! Fork the repo and open a pull request with your improvements.
