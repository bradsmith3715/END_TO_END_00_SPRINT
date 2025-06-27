import streamlit as st
from openai import OpenAI
from groq import Groq
from google import genai

from core.config import config

## Lets create a sidebar with a dropdown for the model list and providers
with st.sidebar:
    st.title("Settings")

    #Dropdown for model
    provider = st.selectbox("Provider", ["OpenAI", "Groq", "Google"])
    if provider == "OpenAI":
        model_name = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o"])
    elif provider == "Groq":
        model_name = st.selectbox("Model", ["llama-3.3-70b-versatile"])
    else:
        model_name = st.selectbox("Model", ["gemini-2.0-flash"])

    # Save provider and model to session state
    st.session_state.provider = provider
    st.session_state.model_name = model_name


if st.session_state.provider == "OpenAI":
    client = OpenAI(api_key=config.OPENAI_API_KEY)
elif st.session_state.provider == "Groq":
    client = Groq(api_key=config.GROQ_API_KEY)
else:
    client = genai.Client(api_key=config.GOOGLE_API_KEY)


def run_llm(client, messages, max_tokens=500):
    if st.session_state.provider == "Google":
        return client.models.generate_content(
            model=st.session_state.model_name,
            contents=[message["content"] for message in messages],
        ).text
    else:
        return client.chat.completions.create(
            model=st.session_state.model_name,
            messages=messages,
            max_tokens=max_tokens
        ).choices[0].message.content



if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hello! How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        output = run_llm(client, st.session_state.messages)
        st.write(output)
    st.session_state.messages.append({"role": "assistant", "content": output})