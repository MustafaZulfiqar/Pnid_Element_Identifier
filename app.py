import streamlit as st
from io import BytesIO
import google.generativeai as genai
import requests

API_KEY = "YOUR_API_KEY_HERE"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
response = requests.get(url)
data = response.json()

# Print available models
for model in data.get("models", []):
   st.write(model["name"])
