# LLM related libraries
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
# API related libraries
import uvicorn
from fastapi import FastAPI
from langserve import add_routes
# Misc Libraries
import os

#-------- Set all the API KEY --------------------------------#
#-------------------------------------------------------------#
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true" # Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
#-------------------------------------------------------------#

#---------- Create the app ------------------------------------#
app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = " API Server for Chatbot"
)

#---------- Create the routes ------------------------------------#
add_routes(
    app,
    ChatOpenAI(),
    path = "/openAI"
)

llm_openai = ChatOpenAI()
llm_llama2 = Ollama(model = "llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an haiku about {topic}")

add_routes(
    app,
    prompt1|llm_openai,
    path = '/essay'
)

add_routes(
    app,
    prompt2|llm_llama2,
    path = '/haiku'
)

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8080)