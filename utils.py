from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv

load_dotenv()


def init_llm():
    llm =ChatOpenAI(model="gpt-4o-mini", openai_api_key=os.getenv('OPENAI_API_KEY'),temperature = 0)
    return llm
