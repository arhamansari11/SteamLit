import streamlit as st

st.title("Hackathon App")


image_url = "https://images.datacamp.com/image/upload/v1640050215/image27_frqkzv.png"
st.markdown(f"""
    <div style="text-align: center;">
        <img src="{image_url}" style="width: 300px; height: auto;">
    </div>
    """, unsafe_allow_html=True)

input_text = st.text_area("Enter any text we will print: ")

if st.button("Print"):
    st.write(input_text)
