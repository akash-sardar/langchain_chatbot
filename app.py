# Langchain Libraries
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Streamlit for UI
import streamlit as st
import os

# to import libraries
from dotenv import load_dotenv

#-------- Set all the API KEY --------------------------------#
#-------------------------------------------------------------#
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true" # Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
#-------------------------------------------------------------#

#--------- Prompt Template -----------------------------------#
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful AI assisstant. Please respond to the user queries"),
        ("user", "Question : {question}")
    ]
)
#-------------------------------------------------------------#

#---------- setup Streamlit framework ------------------------#
st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want")
#-------------------------------------------------------------#

#----------- Initiate OpenAI LLM---------------------------------------#
llm = ChatOpenAI(model= "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
#-----------------------------------------------------------------------#

#------------ Invoke LANGCHAIN -----------------------------------------#
if input_text:
    st.write(chain.invoke({"question": input_text}))
#-----------------------------------------------------------------------#



