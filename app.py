import streamlit as st
import os
#from dotenv import load_dotenv

# Streamlit Cloud では `st.secrets` を使い、ローカルでは `.env` を使用
#try:
os.environ["OPENAI_API_KEY"]  = st.secrets["OPENAI_API_KEY"]  
# Streamlit Cloud
#except FileNotFoundError:
#    load_dotenv()
#    api_key = os.getenv("OPENAI_API_KEY", "")

st.title("専門家に相談できます")
st.write("#### 相談する専門ジャンルを選んでください")
st.write("ラジオボタンで専門ジャンルを選んでください")
st.write("#### 相談内容を入力フォームに入力してください")

