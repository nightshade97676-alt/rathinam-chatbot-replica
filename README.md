# Groq Chatbot Replica

🤖 A high-performance conversational chatbot built using **Streamlit** and **Groq API**, replicating the popular Groq chatbot with LangChain integration.

## Features ✨

- 🚀 **Fast Responses**: Powered by Groq's Language Processing Unit (LPU) for ultra-low latency
- 💬 **Conversational Memory**: Maintains context across messages with configurable memory length
- 🎨 **Streamlit UI**: Beautiful and intuitive user interface
- 🔧 **Model Selection**: Choose from multiple LLM models (Llama, Gemma, Mixtral)
- 🎯 **Customizable Prompts**: Set system prompts to customize chatbot behavior
- 🔐 **Secure API Key**: Password-protected API key input

## Installation 🛠️

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A Groq API key (get it free at [Groq Console](https://console.groq.com/keys))

### Step 1: Clone the Repository

```bash
git clone https://github.com/nightshade97676-alt/rathinam-chatbot-replica.git
cd rathinam-chatbot-replica
```

### Step 2: Create a Virtual Environment

**On Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/keys)
2. Sign up or log in to your account
3. Generate a new API key
4. Copy the API key

## Running the Application 🚀

```bash
streamlit run app.py
```

The app will open in your web browser at `http://localhost:8501`

## Usage Instructions 📖

1. **Enter Your API Key**: Paste your Groq API key in the sidebar (it won't be saved)
2. **Choose a Model**: Select your preferred LLM model from the dropdown
3. **Customize System Prompt**: Optionally modify the system prompt to change bot behavior
4. **Set Memory Length**: Adjust how many previous messages the chatbot remembers
5. **Ask Questions**: Type your questions in the input box and press Enter

## Available Models

- **gemma2-9b-it** - Gemma 2 9B (8,192 tokens)
- **gemma-7b-it** - Gemma 7B (8,192 tokens)
- **llama3-groq-8b-8192-tool-use-preview** - Llama 3 with tool use (8,192 tokens)
- **llama-3.1-70b-versatile** - Llama 3.1 70B (131,072 tokens) ⭐
- **llama-3.1-8b-instant** - Llama 3.1 8B (131,072 tokens)
- **llama-guard-3-8b** - Llama Guard for safety (8,192 tokens)
- **llama3-70b-8192** - Meta Llama 3 70B (8,192 tokens)
- **llama3-8b-8192** - Meta Llama 3 8B (8,192 tokens)
- **mixtral-8x7b-32768** - Mixtral 8x7B (32,768 tokens)

## Project Structure

```
rathinam-chatbot-replica/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── README.md             # This file
└── .gitignore           # Git ignore file
```

## Dependencies

- **streamlit** - Web UI framework
- **groq** - Groq API client
- **langchain** - LLM orchestration
- **langchain-core** - Core LangChain functionality
- **langchain-groq** - LangChain Groq integration

## Troubleshooting 🔧

### "API Key is required"
- Make sure you've entered a valid Groq API key
- Check that your API key hasn't expired at [Groq Console](https://console.groq.com/keys)

### "Service is currently unavailable"
- Groq API is temporarily down. Try again later.
- Check your internet connection

### "ModuleNotFoundError"
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

## Original Source

This is a replica of the popular Groq chatbot by [SauravSrivastav](https://github.com/SauravSrivastav/groqchatbot)

## License

MIT License - See LICENSE file for details

## Contact & Support 📞

For issues and feature requests, please create an issue on GitHub.

---

**Happy Chatting! 🎉**
