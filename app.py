import streamlit as st
from datetime import datetime

# Initialize session state for chat history and logs
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'logs' not in st.session_state:
    st.session_state.logs = []

# Function to handle sending a message
def send_message():
    user_message = st.session_state.user_input
    if user_message:
        st.session_state.chat_history.append(f"You: {user_message}")
        st.session_state.logs.append(f"{datetime.now()} - User: {user_message}")
        # Here you would add the logic to get the chatbot response
        bot_response = "This is a placeholder response."
        st.session_state.chat_history.append(f"Bot: {bot_response}")
        st.session_state.logs.append(f"{datetime.now()} - Bot: {bot_response}")
        st.session_state.user_input = ""

# Streamlit app layout
st.title("Chatbot App")

# Chat window
st.subheader("Chat")
chat_window = st.empty()
chat_window.text_area("Chat", value="\n".join(st.session_state.chat_history), height=300, disabled=True)

# Input area and send button
st.text_input("Your message:", key="user_input", on_change=send_message)
st.button("Send", on_click=send_message)

# Logs subwindow
st.subheader("Logs")
logs_window = st.empty()
logs_window.text_area("Logs", value="\n".join(st.session_state.logs), height=200, disabled=True)