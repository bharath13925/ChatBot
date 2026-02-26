## since i don't have open ai credits so i use the ollama version in .ipynb files the openai code be there for reference 
# for execution this code should be used as named as same file name but sit should be replaced with .ipynb as .py

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

## Streamlit UI
st.title("LangChain Demo With OLLAMA")
input_text = st.text_input("Search the topic you want")

# Ollama LLM
llm = ChatOllama(
    model="llama3",   # Make sure you pulled this model
    temperature=0.7
)

output_parser = StrOutputParser()

# LCEL Chain
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)