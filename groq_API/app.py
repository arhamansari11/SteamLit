import streamlit as st
from groq import Groq

# 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

# Initialize Groq client
client = Groq(
    api_key=""
)

# Streamlit app title
st.title("GEN-AI App Using groq_Api")

# Define the prompt and model
prompt = st.text_input("Enter your Text:")
model_name = "llama3-8b-8192"

# Function to call the groq API and return the completion response
def get_chat_completion(prompt, model_name):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model_name,
    )
    return chat_completion.choices[0].message.content

# Display the prompt and result in Streamlit
# st.write("Prompt:", prompt)

# Button to generate response
if st.button("Generate Response"):
    with st.spinner('Generating response...'):
        # Fetching response from groq API
        response = get_chat_completion(prompt, model_name)
        # Displaying the response in Streamlit
        # st.success("Response generated successfully!")
        st.write(response)
