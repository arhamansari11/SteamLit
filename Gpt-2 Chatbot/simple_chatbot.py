import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

# Hardcode the HuggingFace API token
# HF_TOKEN = 

# Initialize the HuggingFace endpoint
repo_id = "openai-community/gpt2"
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token="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")

# Set up Streamlit UI
st.title("Simple Chatbot")

# Get user input
user_input = st.text_input("You:", "Type your message...")

if st.button("Submit"):
    if user_input:
        # Generate response from the model
        response = llm.invoke(user_input)
        st.text_area("Bot:", response, height=200)
    else:
        st.error("Please enter a message.")
