#The prompt templates
from langchain_core.prompts import ChatPromptTemplate
#StrOutputParser is the default output parser
from langchain_core.output_parsers import StrOutputParser

#Third party integration using langchain community , embeddings 
from langchain_community.llms import Ollama

import streamlit as st
import os

#loading .env files
from dotenv import load_dotenv
load_dotenv()

#langchain api key will help with monitoring i.e.. Langmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title('Langchain Demo with Local llama model')
input_text=st.text_input("Search the topic you want")

output_parser=StrOutputParser()

# local LLms using Ollama
llm=Ollama(model="llama2")

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))