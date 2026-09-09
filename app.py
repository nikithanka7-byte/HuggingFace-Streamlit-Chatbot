import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.caption("Powered by Hugging Face")

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"],
    provider="auto"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("💬 Chat")
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.write("Ask me anything!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Message AI...")

if question:

    st.chat_message("user").write(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful, friendly and intelligent AI assistant. Give simple and clear answers."
                    }
                ] + st.session_state.messages
            )

            answer = response.choices[0].message.content

            st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })