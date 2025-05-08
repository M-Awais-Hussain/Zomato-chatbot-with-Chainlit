import chainlit as cl
from src.llm import ask_order, messages  # 'messages' is the shared message list

@cl.on_message
async def main(message: cl.Message):
    # Append user's message
    messages.append({"role": "user", "content": message.content})

    # Get assistant response
    response = ask_order(messages)

    # Append assistant's reply
    messages.append({"role": "assistant", "content": response})

    # Send response to frontend
    await cl.Message(content=response).send()
