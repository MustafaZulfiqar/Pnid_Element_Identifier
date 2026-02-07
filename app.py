import streamlit as st
from io import BytesIO
import google.generativeai as genai
import requests

API_KEY = "YOUR_API_KEY_HERE"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    models = data.get("models", [])
else:
    st.error(f"Failed to fetch models. Status code: {response.status_code}")
    st.stop()

# Print available models
if models:
    st.subheader("Models your API key can access:")
    for model in models:
        st.write(model["name"])
