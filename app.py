import streamlit as st
import os
#from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

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


selected_genre = st.radio("どの専門家に相談したいかを選択してください", ["和食の専門家","中華の専門家","洋食の専門家"])
input_message = st.text_input(label="相談内容を入力してください。")


if st.button("実行する"):
    st.divider()

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

    message = [
        SystemMessage(content=f"あなたは、料理のプロフェッショナルです。特に、{selected_genre}です。的確なアドバイスができる料理専門家です"),
        HumanMessage(content=input_message)
    ]

    result = llm(message)


    st.write(f"回答：{result.content}")

