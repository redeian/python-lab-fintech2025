from util import print_mult_table
import pandas as pd
import streamlit as st
import requests


st.title("Dashboard")
st.write("This application is about displaying product sales")

# show registered user if available
if 'username' in st.session_state:
    # fixed quoting to avoid syntax error
    st.write(f"Hello! {st.session_state['username']}")
else:
    st.info("please register at setting page.")


upload_file = st.file_uploader("Choose a CSV file", type="csv")

# nbutton will trigger a GET request to the webhook below
nbutton = st.button("ok")

# second button to POST JSON to a local webhook
pbutton = st.button("post")

WEBHOOK_URL = "https://116ae1675f2a.ngrok-free.app/webhook/4ef3a9f4-246a-47e4-8e29-9bafcdec3c93"

if nbutton:
    try:
        with st.spinner("Sending request..."):
            resp = requests.get(WEBHOOK_URL, timeout=5)
        st.success(f"Request finished with status {resp.status_code}")
        # show a small preview of the response body
        preview = resp.text[:500]
        if preview:
            st.code(preview)
    except requests.RequestException as e:
        st.error(f"Request failed: {e}")


POST_URL = "https://116ae1675f2a.ngrok-free.app/webhook/postTV"
POST_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 11111",
}
POST_PAYLOAD = {"name": "Mark", "score": 10}

if pbutton:
    try:
        with st.spinner("Sending POST request..."):
            resp = requests.post(POST_URL, json=POST_PAYLOAD, headers=POST_HEADERS, timeout=5)
        st.success(f"POST finished with status {resp.status_code}")
        preview = resp.text[:500]
        if preview:
            st.code(preview)
    except requests.RequestException as e:
        st.error(f"POST failed: {e}")


# --- Add a form for posting custom name/score ---
with st.form("post_form"):
    form_name = st.text_input("name", value="Mark")
    form_score = st.number_input("score", value=10, step=1)
    form_submit = st.form_submit_button("Send POST")

if form_submit:
    # basic validation
    if not form_name:
        st.error("Please enter a name before submitting.")
    else:
        payload = {"name": form_name, "score": int(form_score)}
        try:
            with st.spinner("Sending POST request..."):
                resp = requests.post(POST_URL, json=payload, headers=POST_HEADERS, timeout=5)
            st.success(f"POST finished with status {resp.status_code}")
            preview = resp.text[:500]
            if preview:
                st.code(preview)
        except requests.RequestException as e:
            st.error(f"POST failed: {e}")


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


