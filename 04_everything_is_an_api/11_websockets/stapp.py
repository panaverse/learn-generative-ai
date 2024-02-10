import streamlit as st
from websocket import create_connection

# URL of the WebSocket
ws_url = "ws://localhost:8000/ws"

# Create a Streamlit interface
st.title('WebSocket Client')

# Input for sending a message
user_input = st.text_input("Send a message to the WebSocket:")

if st.button('Send'):
    # Create a connection to the WebSocket
    ws = create_connection(ws_url)

    # Send the message
    ws.send(user_input)

    # Receive and print the response
    response = ws.recv()
    st.write("Received:", response)

    # Close the WebSocket connection
    ws.close()
