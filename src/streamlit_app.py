import streamlit as st, requests

st.title("🧠 RAG with PDF + Message History")

api_url = "https://0aft1y1h6a.execute-api.us-east-1.amazonaws.com/default/RagPDFBackend"

query = st.text_input("💬 Ask your question:")
if st.button("Submit"):
    response = requests.post(api_url, json={"query": query})
    st.write(response.json()["answer"])
