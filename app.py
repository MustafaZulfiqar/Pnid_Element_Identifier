import streamlit as st
from io import BytesIO
import google.generativeai as genai

st.title("LLM File Processor")
genai.configure(api_key=st.secrets["Google_API"])
model = genai.GenerativeModel("gemini-1.5-flash")


uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

def process_with_llm(text):
    response = model.generate_content(text)
    return response.text

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    if st.button("Send to LLM"):
        with st.spinner("Processing..."):
            result = process_with_llm(text)

        output = BytesIO(result.encode("utf-8"))

        st.download_button(
            "Download processed file",
            data=output,
            file_name="output.txt",
            mime="text/plain"
        )
