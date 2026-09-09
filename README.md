#  AI Chatbot - hugging face & streamlit

##  Project Description

This project is a simple AI chatbot developed using Streamlit and a Large Language Model accessed through Hugging Face Inference.

The chatbot allows users to ask questions and receive AI-generated responses through a simple ChatGPT-style interface.

##  Objective

The main objective of this project is to learn how to access a Large Language Model programmatically using the Hugging Face API and integrate it with a Streamlit application.

##  Technologies Used

- Python
- Streamlit
- Hugging Face
- Hugging Face InferenceClient
- Large Language Model

##  Model Used

`openai/gpt-oss-120b`

The model is accessed through Hugging Face Inference Providers.


---

## **Architecture**

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
```

---

## **Features**

*  ChatGPT-style chat interface
*  User and AI messages
*  Chat history
*  Clear Chat option
*  Hugging Face LLM integration
*  Simple and user-friendly interface
*  AI-generated responses

---

## **Project Structure**

```text
HuggingFace_LLM/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/nikithanka7-byte/HuggingFace-Streamlit-Chatbot.git
```

### **2. Install Required Packages**

```bash
pip install -r requirements.txt
```

---

## **Hugging Face Token Setup**

Create a **Hugging Face Access Token**.

For **Windows PowerShell**:

```powershell
$env:HF_TOKEN="your_huggingface_token"
```

>  **Important:** Do not upload your Hugging Face token to GitHub.

---

## **Run the Application**

Run the following command:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## **Example**  - Application preview

[streamlit-app-2026-09-09-23-34-18.webm](https://github.com/user-attachments/assets/159ebfa4-e2ff-44eb-8b6b-f3aa2314f78b)


---

## **Learning Outcome**

This project demonstrates how to:

* Connect Python with Hugging Face.
* Access an LLM programmatically.
* Use an API token securely.
* Build a chatbot using Streamlit.
* Maintain chat history.
* Create a simple AI application.

---

## **Author**

**Nikitha R**

---
