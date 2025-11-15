import streamlit as st
import requests
import base64

st.set_page_config(page_title="🧠 RAG with PDF + Memory", page_icon="📄", layout="centered")

st.title("🧠 RAG with PDF + Message History (Serverless via AWS Lambda)")

API_URL = "https://0aft1y1h6a.execute-api.us-east-1.amazonaws.com/default/RagPDFBackend" 

uploaded_file = st.file_uploader("📄 Upload your PDF file", type=['pdf'])

query = st.text_input("💬 Ask your question about the PDF:")

if st.button("Submit"):
    if not uploaded_file:
        st.warning("Please upload a PDF file first.")
        st.stop()

    if not query:
        st.warning("Please enter your question.")
        st.stop()

    pdf_bytes = uploaded_file.read()
    pdf_b64 = base64.b64encode(pdf_bytes).decode('utf-8')

    with st.spinner("🔍 Processing your query..."):
        try:
            response = requests.post(
                API_URL,
                json={"query": query, "pdf_file": pdf_b64},
                timeout=120
            )

            if response.status_code == 200:
                data = response.json()
                st.success("✅ Answer Generated Successfully!")
                st.write("### 🤖 Assistant's Response:")
                st.write(data.get("answer", "No answer found."))
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Connection error: {e}")

st.markdown("---")
st.caption("Built using LangChain, Groq, Streamlit & AWS Lambda")
