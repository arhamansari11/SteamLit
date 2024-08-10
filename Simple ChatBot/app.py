# AIzaSyDqenQKdz1vK5lWPdyTKjVR6rcEy_A9-uQ
import google.generativeai as genai

import streamlit as st

# GOOGLE_API_KEY = "AIzaSyDqenQKdz1vK5lWPdyTKjVR6rcEy_A9-uQ"

# genai.configure(api_key=GOOGLE_API_KEY)

# StreamLit Tite
st.set_page_config(page_title="Simple ChatBot", layout="centered") 

st.title("✨Simple ChatBot✨")

st.write("Powered by Google Generative AI")


# Model Initiate

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text



with st.form(key="chat_form" , clear_on_submit=True):
    user_input = st.text_input("Enter your query? " )
    submit_button = st.form_submit_button("Send")


    if submit_button:
        if user_input:
            response = getResponseFromModel(user_input)
            st.write(response)
        else:
            st.warning("Please Enter Some text.")













# user_input = input("Enter your Prompt : ")

# output = getResponseFromModel(user_input)

# print(output)

