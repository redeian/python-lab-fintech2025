from util import print_mult_table
import pandas as pd
import streamlit as st


st.title("Dashboard")
st.write("This application is about displaying product sales")

if 'username' in st.session_state:
    st.write(f'Hello! {st.session_state['username']}')
else:
    st.info("please register at setting page.")


upload_file = st.file_uploader("Choose a CSV file", type="csv")

if upload_file is None:
    st.write("please upload csv file.")

else:

    data = pd.read_csv(upload_file)

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


