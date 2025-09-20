from util import print_mult_table
import pandas as pd
import streamlit as st

data = pd.read_csv("products.csv")

st.title("Dashboard")
st.write("This application is about displaying product sales")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Sales", "1,200", "12%")
with col2:
    st.metric("Revenue", "100,200", "10%")
with col3:
    st.metric("Users", "120", "12%")


st.line_chart(data['sales'])

if st.checkbox("show table"):
    st.header("Sales table")
    st.subheader("This is a sales table")
    st.write(data)


