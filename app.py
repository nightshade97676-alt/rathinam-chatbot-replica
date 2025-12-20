import streamlit as st
from groq import Groq

# Page title and description
st.set_page_config(page_title="Simple Groq Chatbot", layout="wide")
st.title("🤖 Simple Groq Chatbot")
st.write("A beginner-friendly chatbot using Groq API")

# Sidebar - API Key Input
st.sidebar.title("Settings")
st.sidebar.write("Get your free API key from [Groq Console](https://console.groq.com/keys)")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Check if API key is provided
if not api_key:
    st.error("❌ Please enter your Groq API Key to start chatting")
    st.stop()

# Initialize Groq client
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # Get response from Groq API
    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=st.session_state.chat_history,
            max_tokens=1024
        )
        
        assistant_message = response.choices[0].message.content
        
        # Add assistant message to history
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})
        st.chat_message("assistant").write(assistant_message)
        
    except Exception as e:
        st.error(f"Error: {e}")

# Clear chat button
if st.sidebar.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()
