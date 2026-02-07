import streamlit as st
from io import BytesIO
import google.generativeai as genai

st.title("LLM File Processor")
genai.configure(api_key="AIzaSyCsy6rECIf_4xT9_Bnp9eooqrm47gM3GYw")

model = genai.GenerativeModel("Gemini 2.0 Flash-Lite")


#uploaded_file = st.file_uploader("Upload a text file", type=["txt"])


# Text input
question = st.text_input("Ask a question")

def ask_llm(question: str) -> str:
    response = model.generate_content(question)
    return response.text


# Button
if st.button("Ask"):
    answer = ask_llm(question)
    st.subheader("Answer")
    st.write(answer)

import requests

API_KEY = "AIzaSyCsy6rECIf_4xT9_Bnp9eooqrm47gM3GYw"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
response = requests.get(url)
data = response.json()

# Print available models
for model in data.get("models", []):
    print(model["name"])

#if uploaded_file:
 #   text = uploaded_file.read().decode("utf-8")

  #  if st.button("Send to LLM"):
   #     with st.spinner("Processing..."):
    #        result = process_with_llm(text)

     #   output = BytesIO(result.encode("utf-8"))

      #  st.download_button(
            #"Download processed file",
            #data=output,
            #file_name="output.txt",
            #mime="text/plain"
        #)
