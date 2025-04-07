import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Service account for Gemini
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"c:\Users\Asus\Downloads\golden-ripsaw-449920-v1-54ec8b382164.json"


### 1. PDF Reader
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


### 2. Text Splitter
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return splitter.split_text(text)


### 3. Vector Store
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


### 4. Conversational Chain (Q&A)
def get_conversational_chain():
    prompt_template = """
    You are a legal assistant. Answer the question using only the context below.
    Be accurate and include all relevant legal details. If not found, say "Not available in context."

    Context: {context}
    Question: {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-001", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)


def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("📌 Answer:", response["output_text"])


### 5. Summarize Document
def summarize_document(text):
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-001", temperature=0.3)
    summary_prompt = f"""
    Summarize this legal contract for a general understanding, highlighting important sections such as:
    - Obligations
    - Payment terms
    - Term & Termination
    - Confidentiality
    - Penalties

    Use clean formatting with bullet points and section headers.

    Contract Text:
    {text[:10000]}

    Summary:
    """
    response = model.invoke(summary_prompt)
    return response.content if hasattr(response, "content") else str(response)


### 6. Risky Clause Detection
def extract_risky_clauses(text):
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-001", temperature=0.3)
    clause_prompt = f"""
    From the following legal contract text, extract and list **risky or sensitive clauses** related to:
    - Termination
    - Indemnity
    - Confidentiality
    - Penalties
    - Limitation of Liability

    For each clause, provide:
    1. **Clause Type**
    2. **Exact Clause Text**
    3. **Why it may be risky**

    Format the output clearly with headers and bullets.

    Text:
    {text[:10000]}

    Risky Clauses:
    """
    response = model.invoke(clause_prompt)
    return response.content if hasattr(response, "content") else str(response)


### MAIN APP
def main():
    st.set_page_config("Legal Document Assistant")
    st.header("📄 Legal Document Assistant (Contract Analyzer)")

    with st.sidebar:
        st.title("Upload & Process Contract")
        pdf_docs = st.file_uploader("Upload Legal PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process") and pdf_docs:
            with st.spinner("Reading and processing contract..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.session_state['text'] = raw_text
                st.success("✅ Document Processed")

    # Summary Tab
    if "text" in st.session_state:
        tab1, tab2, tab3 = st.tabs(["📃 Summary", "⚠️ Risky Clauses", "❓Ask a Question"])

        with tab1:
            st.subheader("📃 Document Summary")
            summary = summarize_document(st.session_state['text'])
            st.markdown(summary)

        with tab2:
            st.subheader("⚠️ Risky Clauses Identified")
            clauses = extract_risky_clauses(st.session_state['text'])
            st.markdown(clauses)


        with tab3:
            st.subheader("Ask Questions about the Contract")
            question = st.text_input("Ask your legal question (e.g., What are the termination conditions?)")
            if question:
                user_input(question)


if __name__ == "__main__":
    main()
