import os

from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
)

chat_model = ChatHuggingFace(llm=llm)


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms."
)

parser = StrOutputParser()

chain = prompt | chat_model | parser