# import streamlit as st
# import openai
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # Set up OpenAI client
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def translate_to_urdu(text):
#     prompt = f"Translate the following text to Urdu: {text}"

#     response = openai.Completion.create(
#         model="text-davinci-003",  # Use a valid model name
#         prompt=prompt,
#         max_tokens=150
#     )

#     return response.choices[0].text.strip()

# st.title("Translate to Urdu")

# input_text = st.text_area("Enter text in any language:")
# if st.button("Translate"):
#     if input_text:
#         urdu_translation = translate_to_urdu(input_text)
#         st.write("Urdu Translation:")
#         st.write(urdu_translation)
#     else:
#         st.warning("Please enter some text to translate.")

import streamlit as st

st.title("Print the Input Texts")

# Create a text area for user input
input_text = st.text_area("Enter your text:")

# Create a button that prints the text when clicked
if st.button("Print"):
    # Display the input text
    st.write( input_text)
