from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

result=chat_model.invoke("안녕!")
print(result.content)


import streamlit as st
st.title("인공지능 시인")
