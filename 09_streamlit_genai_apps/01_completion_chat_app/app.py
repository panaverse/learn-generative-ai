from model import BotModel
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()

st.title("Streamlit Chatbot Math Tutor")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"


if "bot" not in st.session_state:
    st.session_state["bot"] = BotModel("My Chatbot")

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state["bot"].delete_chat_history()

# Display chat messages
for message in st.session_state.bot.get_messages():
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("How can I help?"):

    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""
        for response in st.session_state.bot.send_message({"role": "user", "content": prompt}):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
    st.session_state.bot.messages.append({"role": "assistant", "content": full_response})

# Save chat history after each interaction
st.session_state.bot.save_chat_history()