# https://docs.streamlit.io/library/api-reference/chat/st.chat_input

import streamlit as st

prompt = st.chat_input("Say something")
data : list = []
if prompt:
    data.append(prompt)
    st.write(f"User has sent the following prompt: {prompt}")

st.write(data)