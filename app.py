import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an helpful AI assistant.Please respond to the query asked."),
        ("user","Question:{question}")
    ]
)

# StreamLit Framework
st.title("Langchain AI Assistant")
input_text = st.text_input('What is you query?')

#OpenAI Model
llm = ChatOpenAI(model='gpt-4o')
output = StrOutputParser()
chain = prompt | llm | output

if input_text:
    st.write(chain.invoke({'question':input_text}))