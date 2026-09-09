#  Hugging Face AI Chatbot

##  Project Description

This project is a simple AI chatbot developed using Streamlit and a Large Language Model accessed through Hugging Face Inference.

The chatbot allows users to ask questions and receive AI-generated responses through a simple ChatGPT-style interface.

##  Objective

The main objective of this project is to learn how to access a Large Language Model programmatically using the Hugging Face API and integrate it with a Streamlit application.

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face
- Hugging Face InferenceClient
- Large Language Model

##  Model Used

`openai/gpt-oss-120b`

The model is accessed through Hugging Face Inference Providers.

##  Architecture

```text
User
  ↓
Streamlit Chat Interface
  ↓
Python Application
  ↓
Hugging Face Inference API
  ↓
LLM Model
  ↓
AI Response
  ↓
Streamlit Interface
## Features

- ChatGPT-style chat interface
- User and AI messages
- Chat history
- Clear Chat option
- Hugging Face LLM integration
- Simple and user-friendly interface
- AI-generated responses

## Project Structure

```text
HuggingFace_LLM/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

Installation

Clone the repository:

git clone - https://github.com/nikithanka7-byte/HuggingFace-Streamlit-Chatbot

Install required packages:

pip install -r requirements.txt

 Hugging Face Token Setup

Create a Hugging Face Access Token.

For Windows PowerShell:

$env:HF_TOKEN="your_huggingface_token"

Do not upload your Hugging Face token to GitHub.

 Run the Application
python -m streamlit run app.py

The application will open in the browser.

 Example :[streamlit-app-2026-09-09-23-34-18.webm](https://github.com/user-attachments/assets/f05de5a4-58bf-4e0c-95b6-673c644a7ad5)

 Learning Outcome

This project demonstrates how to:
Connect Python with Hugging Face.
Access an LLM programmatically.
Use an API token securely.
Build a chatbot using Streamlit.
Maintain chat history.
Create a simple AI application.

---
 Author
Nikitha R
