import streamlit as st

st.set_page_config(
    page_title="Ractangle Page",
    layout="wide"
)

st.title("Rectangle")

width = st.number_input("width")
height = st.number_input("height")
if st.button("cal rectangle area"):
    st.write(f'area = {width * height}')