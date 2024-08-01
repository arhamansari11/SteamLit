import streamlit as st

# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code)


# try_code = ''' def function():
#     print("I am Muhammad Arham") '''

variable  = "I am Muhammad Arham and I am a MERN Stack Develoepr"
st.code(variable)
# st.code(try_code)
# st.header("Hello World !")
# st.title("Hello World !")
# st.caption("Hello World !")

st.write("This is some text")

st.slider("This is Slider" , 0 , 100 , (25,75))

st.divider()
st.write("This is Divider")
st.divider()


