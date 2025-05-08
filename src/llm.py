from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from src.prompt import system_instruction

import os
from dotenv import load_dotenv

load_dotenv()

# Initialize ChatGroq client
client = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # you can also try mixtral-8x7b-32768 or gemma-7b-it
    temperature=0
)

# Message history to be maintained
messages = [
    {"role": "system", "content": system_instruction}
]

# Function to send messages with full history
def ask_order(messages: list):
    langchain_messages = []

    for msg in messages:
        if msg["role"] == "system":
            langchain_messages.append(SystemMessage(content=msg["content"]))
        elif msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            langchain_messages.append(AIMessage(content=msg["content"]))

    response = client(langchain_messages)
    return response.content
