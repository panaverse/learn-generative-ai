import streamlit as st 
from model import OpenAIBot, MessageItem

st.set_page_config(page_title="Math Tutor", page_icon=":speech_balloon:")

st.title('Math Tutor')
st.write("Tutor Will Help You Answer Math Questions")

if "bot" not in st.session_state:
    st.session_state.bot = OpenAIBot("Math Tutor", 
        instructions="You are a personal math tutor. Write and run code to answer math questions.")


for m in st.session_state.bot.getMessages():
    with st.chat_message(m.role):
        st.markdown(m.content)

if prompt := st.chat_input("Please Ask a Question"):
    st.session_state.bot.send_message(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    if(st.session_state.bot.isCompleted()):
        response: MessageItem = st.session_state.bot.get_lastest_response()
        with st.chat_message(response.role):
            st.markdown(response.content)