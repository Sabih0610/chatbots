import gradio as gr
import requests
import json  # <-- ADD THIS LINE

print("Script is running!")

MODEL_NAME = "llama3"  # Or "mixtral" or "phi3"

def chat_with_ollama(message, history):
    prompt = "\n".join([f"User: {m[0]}\nAI: {m[1]}" for m in history] + [f"User: {message}\nAI:"])
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": MODEL_NAME, "prompt": prompt},
        stream=True  # <-- IMPORTANT: streaming enabled
    )
    output = ""
    for line in response.iter_lines():
        if line:
            data = line.decode('utf-8')
            try:
                obj = json.loads(data)
                if "response" in obj:
                    output += obj["response"]
            except Exception as e:
                print("Line decode error:", e, "| Line:", data)
    return output

iface = gr.ChatInterface(
    chat_with_ollama,
    title="My Local Chatbot",
    description="Chat with a local open-source LLM running on your PC using Ollama!"
)
iface.launch()
