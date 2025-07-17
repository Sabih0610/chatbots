@"
# Local AI Chatbot 🚀

A fully local, private ChatGPT-style chatbot running on your own PC.  
Built with open-source LLMs (Llama 3, Mixtral, Phi-3, and more) using [Ollama](https://ollama.com/) and [Gradio](https://gradio.app/).

---

## Features

- Run Llama 3, Mixtral, Phi-3, Gemma, and other models locally
- Chat with your AI using a friendly web interface
- No API keys, no cloud – 100% private and offline
- Simple Python code, easy to modify

---

## Prerequisites

- Windows, macOS, or Linux
- Python 3.10 or newer ([download Python](https://www.python.org/downloads/))
- [Ollama](https://ollama.com/download) (download and install for your OS)
- Basic command line usage

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/your-github-username/chatbots.git
cd chatbots

2. Set up a Python virtual environment

python -m venv venv
Window
.\venv\Scripts\activate 
macOS/Linux:
 venv/bin/activate
3.Install Python requirements
 pip install -r requirements.txt


4. Install and start Ollama
Download Ollama here and install it.

Start Ollama:

Windows: Open Ollama from the Start Menu

macOS/Linux: Run in terminal:

 ollama serve
5. Pull a model (example: Llama 3)
 ollama pull llama3
You can also pull other models (pick one, or try them all!):

 ollama pull mixtral
 ollama pull phi3
 ollama pull gemma:2b
See all models here

6. Check that your model is available
 ollama list
You should see the model(s) you pulled in the list.
 Running the Chatbot

Make sure your virtual environment is activated and Ollama is running.
 python app.py
Open your browser and go to http://localhost:7860

Start chatting!

