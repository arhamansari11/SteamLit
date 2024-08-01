# import streamlit as st
# st.title("First StreamLit App")
# input_text = st.text_area("Enter your text : ")
# if st.button("Print"):
#     st.write(input_text)
import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code)


try_code = ''' def function():
    print("I am Muhammad Arham") '''

variable  = "I am Muhammad Arham and I am a MERN Stack Develoepr"
st.code(variable)
st.code(try_code)
st.header("Hello World !")
st.title("Hello World !")
st.caption("Hello World !")