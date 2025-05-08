# 🍕 Zomato Chatbot with Chainlit

An **AI-powered chatbot** built using **Chainlit** and **LangChain (Groq API)** that acts as an interactive order assistant for Zomato.  
It can **greet customers, take detailed orders, clarify options, handle delivery or pickup, summarize the order, and collect payment** — all in a friendly, conversational style.

---

## ✨ Features

✅ Interactive Zomato ordering chatbot  
✅ Menu includes pizzas, pasta, Asian & Indian dishes, beverages  
✅ Clarifies order details (sizes, extras, options)  
✅ Handles both **pickup** and **delivery** (with address collection)  
✅ Calculates totals & confirms before payment  
✅ Runs as a live Chainlit app with real-time chat interface

---

## 🚀 How to Run

1️⃣ **Install dependencies**
```
pip install chainlit langchain langchain-groq python-dotenv
```
2️⃣ **Set up your .env file**
```
GROQ_API_KEY=your_groq_api_key_here
```
3️⃣ **Start the Chainlit app**
```
chainlit run main.py
````

---

## 📝 Example Prompt
User: Hi, I’d like to order a Pepperoni Pizza and a Coke.
Bot: Great choice! That’s one 12-inch Pepperoni Pizza ($10.99) and one Coke can ($1.50). Is this for pickup or delivery?

---
 
## 🛠️ Technologies Used
Chainlit → Live chatbot frontend

LangChain → LLM message management

Groq API (LLaMA3) → Fast large language model backend

Python → Core application

dotenv → API key management

---
