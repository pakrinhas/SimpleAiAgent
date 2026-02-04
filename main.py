from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import  ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()  # Load environment variables from .env file

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]



llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")  # Example model name
parser = PydanticOutputParser(pydantic_object=ResearchResponse)
