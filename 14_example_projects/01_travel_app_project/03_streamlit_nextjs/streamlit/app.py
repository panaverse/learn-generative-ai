import streamlit as st
import plotly.graph_objects as go
import requests
import json
import os
from streamlit_lottie import st_lottie
from dotenv import load_dotenv, find_dotenv

# Load environment variables
_: bool = load_dotenv(find_dotenv())  # read local .env file
MAPBOX_ACCESS_TOKEN = os.environ.get("MAPBOX_TOKEN")
BACKEND_FASTAPI_URL = os.environ.get("BACKEND_FASTAPI_URL")

# Function to fetch messages from the API
def fetch_runtime_messages():
    try:
        response = requests.get(
            f"{BACKEND_FASTAPI_URL}/openai-streaming/get-all-messages-before-saved")
        response.raise_for_status()  # Raise an exception for HTTP errors
        print('response.json()[1:] ', len(response.json()))
        # Return the parsed JSON data except for the SYSTEM SEED MESSAGE
        return response.json()[1:]
    except requests.RequestException as e:
        print(f"Error fetching messages: {e}")
        return []


# Set page configuration
st.set_page_config(page_title="Wandering AI Trips", page_icon="🧠",
                   layout="wide", initial_sidebar_state="expanded")

# Lottie
def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url


hi_robot = import_json(r"./hi_robot.json")
st_lottie(hi_robot, height=400, key="hey_robot")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

# Initialize session state
if "map_state" not in st.session_state:
    st.session_state.map_state = {
        "markers_state": {"latitudes": [], "longitudes": [], "labels": []},
        "map_state": {"latitude": 39.94961, "longitude": -75.150282, "zoom": 16}
    }


# Initialize session state for messages if not already done
if 'messages' not in st.session_state:
    st.session_state.messages = fetch_runtime_messages()

# Update Runtime function
def update_messages():
    new_messages = fetch_runtime_messages()
    if new_messages != st.session_state.messages:
        st.session_state.messages = new_messages

# Function to update map state
def update_map_state():
    response = requests.get(f'{BACKEND_FASTAPI_URL}/openai-streaming/map-coordinates')
    print("MAP CALL")
    if response.status_code == 200:
        st.session_state.map_state = response.json()
        print("RESPONSE", response.json())
        print("MAP STATE", st.session_state.map_state)

# Sidebar for map and deleting chat history
with st.sidebar:
    st.subheader("Chat Controls")
    # Button for deleting chat history
    if st.button("Delete Chat History"):
        res = requests.delete(
            f"{BACKEND_FASTAPI_URL}/openai-streaming/delete-db-state-chat")
        st.toast(res.json(), icon="🗑️")
        update_messages()

    # Map display
    st.subheader("AI Powered Map")
    if st.session_state.map_state:
        figure = go.Figure(go.Scattermapbox(mode="markers"))
        markers_state = st.session_state.map_state.get("markers_state")
        if markers_state:
            figure.add_trace(go.Scattermapbox(
                mode="markers",
                marker=dict(symbol='marker', size=14),
                lat=markers_state["latitudes"],
                lon=markers_state["longitudes"],
                text=markers_state["labels"],
                hovertemplate=(
                    "<b>%{text}</b><br>Latitude: %{lat}<br>Longitude: %{lon}<extra></extra>")
            ))

        map_state = st.session_state.map_state.get("map_state")
        if map_state:
            figure.update_layout(mapbox=dict(
                accesstoken=MAPBOX_ACCESS_TOKEN,
                center=go.layout.mapbox.Center(
                    lat=map_state["latitude"], lon=map_state["longitude"]),
                zoom=map_state["zoom"]
            ), margin=dict(l=0, r=0, t=0, b=0))

        st.plotly_chart(
            figure, config={"displayModeBar": False}, use_container_width=True)


# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("Let's visit Japan?"):

    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""
        with requests.get(f"{BACKEND_FASTAPI_URL}/openai-streaming/?query={prompt}", stream=True) as r:
            for chunk in r.raw.stream(decode_content=True):
                if chunk:
                    print('chunk', chunk)
                    full_response += chunk.decode("utf-8")
                    message_placeholder.markdown(full_response + "|")
                else:
                    print("No chunks returned...")
                    message_placeholder.markdown("Waiting for response...")
            message_placeholder.markdown(full_response)
    update_messages()
    # Update map state and force Streamlit to rerender the map
    update_map_state()
    st.rerun()

# Save chat history after each interaction
requests.get(f"{BACKEND_FASTAPI_URL}/openai-streaming/save-db-chat")