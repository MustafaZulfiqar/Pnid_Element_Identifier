import streamlit as st
import google.generativeai as genai

st.title("Ask Gemini")

# Configure the API key
genai.configure(api_key="YOUR_API_KEY_HERE")  # Or st.secrets["Google_API"]

# Free-tier model
model = genai.GenerativeModel("gemini-2.5-flash")

def ask_llm(question: str) -> str:
    question = str(question).strip()
    if not question:
        return "Please enter a question."
    response = model.generate_content(question)
    return response.text

# Text input
question = st.text_input("Ask a question")

# Button to query
if st.button("Ask"):
    with st.spinner("Thinking..."):
        answer = ask_llm(question)
    st.subheader("Answer")
    st.write(answer)

