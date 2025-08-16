# chatBot_UI.py
import streamlit as st
import requests
import time

API_URL = "http://localhost:8000/generate"  # Backend running in Jupyter

st.set_page_config(page_title="TinyLlama Chat", page_icon="🤖")
st.title("🤖 TinyLlama Local Chat (Streaming)")
st.write("Running TinyLlama locally with a typing effect...")

# Session state to hold chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Assistant:** {text}")

# User input box
user_input = st.text_input("Enter your message:", key="input")

if st.button("Send") and user_input:
    # Save user message
    st.session_state.messages.append(("user", user_input))

    # Request backend
    with st.spinner("Assistant is thinking..."):
        try:
            resp = requests.post(API_URL, json={"prompt": user_input})
            if resp.status_code == 200:
                full_response = resp.json()["response"]
            else:
                full_response = "⚠️ Error from API"
        except Exception as e:
            full_response = f"⚠️ Connection error: {e}"

    # Stream response (typing effect)
    placeholder = st.empty()
    streamed_text = ""
    for ch in full_response:
        streamed_text += ch
        placeholder.markdown(f"**Assistant:** {streamed_text}")
        time.sleep(0.02)  # typing speed (adjust if too slow/fast)

    # Save assistant full message
    st.session_state.messages.append(("assistant", full_response))

    # Refresh page to show history
    st.rerun()
    
