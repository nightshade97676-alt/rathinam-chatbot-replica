# Import necessary libraries & Setting up environment variables

import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

###############################################################
#########################  BLOCK 1 ############################
###############################################################

# 1. Load Environment Variables (for local_testing)
load_dotenv()

# 2. Initialize Groq Client
# groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq()

# 3. Page Configuration
st.set_page_config(page_title="Groq Chatbot Replica", page_icon="🤖")
st.title("🤖 Groq Chatbot - Powered by Llama")
st.markdown("**A simple, fast, and smart chatbot for everyone!**")

###############################################################
#########################  BLOCK 2 ############################
###############################################################

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

###############################################################
#########################  BLOCK 3 ############################
###############################################################

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

###############################################################
#########################  BLOCK 4 ############################
###############################################################

# 6. Accept User Input
if prompt := st.chat_input("Ask me anything... 💭"):
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.write(prompt)


###############################################################
#########################  BLOCK 5 ############################
###############################################################

    # 7. Generate a Response from Groq
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fast and accurate Llama 3
            messages=st.session_state.messages, 
            temperature=0.7,  # Balanced creativity and accuracy
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        # Extract the text from the response object
        response = completion.choices[0].message.content
        
        # 8. Display & Save Assistant Response
        with st.chat_message("assistant"):
            st.markdown(response)
            
        st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"❌ Oops! Something went wrong: {e}")

###############################################################
# Sidebar - Additional Features
###############################################################

with st.sidebar:
    st.title("⚙️ Settings")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Info section
    st.info(
        "**ℹ️ About This Chatbot:**\n\n"
        "- Powered by Groq API\n"
        "- Using Llama 3.1 8B Model\n"
        "- Fast responses (ultra-low latency)\n"
        "- No API key required (uses system default)"
    )
    
    st.divider()
    
    # Model info
    st.markdown(
        "**📚 Model Details:**\n\n"
        "- **Model**: Llama 3.1 8B\n"
        "- **Provider**: Meta (via Groq)\n"
        "- **Speed**: Ultra-fast inference\n"
        "- **Context**: Up to 131,072 tokens"
    )
