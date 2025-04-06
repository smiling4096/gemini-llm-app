import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Debug: List available models in the sidebar
st.sidebar.title("🧪 Debug Panel")
st.sidebar.write("Available Models:")
try:
    models = genai.list_models()
    for model in models:
        st.sidebar.write(f"✅ {model.name}")
except Exception as e:
    st.sidebar.error(f"Error fetching models: {e}")

# Streamlit UI
st.title("🤖 Gemini LLM App")
st.write("Ask me anything!")

user_input = st.text_input("Enter your prompt")

if st.button("Generate"):
    if user_input:
        try:
            # ✅ Correct model name from your available list
            model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
            response = model.generate_content(user_input)
            st.subheader("Gemini says:")
            st.write(response.text)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter something to ask.")
