# Chattybot

A simple conversational AI chatbot built with **Python, LangChain, Ollama, and Qwen3 4B**.

Chattybot runs completely **locally on your computer**, so it does not require an OpenAI API key or paid API credits.

---

## Features

- Interactive conversational chatbot
- Maintains conversation history during the session
- Powered by Qwen3 4B(You can use any open models)
- Built using LangChain
- Runs locally using Ollama
- No OpenAI API key required
- Can run without an internet connection after the model is downloaded

---

## Tech Stack

- **Python**
- **LangChain**
- **Ollama**
- **Qwen3 4B**
- **Git & GitHub**

---

## Architecture

```text
                 User
                  │
                  ▼
             Chattybot
                  │
                  ▼
              LangChain
                  │
                  ▼
             ChatOllama
                  │
                  ▼
               Ollama
                  │
                  ▼
             Qwen3 4B
                  │
                  ▼
           Local Computer