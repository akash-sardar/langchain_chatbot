import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8080/essay/invoke",
                             json = {"input": {"topic" : input_text}})
    return response.json()["output"]["content"]


def get_llama2_response(input_text):
    response = requests.post("http://localhost:8080/haiku/invoke",
                             json = {"input": {"topic" : input_text}})
    haiku = response.json()["output"]
    return haiku

#-------------------------------------------------------------#
#---------- setup Streamlit framework ------------------------#
st.title("Frontend client api demo")
input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(get_openai_response(input_text))
    st.write(get_llama2_response(input_text))
#-----------------------------------------------------------------------#


