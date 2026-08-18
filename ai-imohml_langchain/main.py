import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
)

chat_model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are Imoh-AI, an AI assistant specialising in "
        "machine learning, data science, and economics."
    ),
    (
        "human",
        "{message}"
    )
])

parser = StrOutputParser()

chain = prompt | chat_model | parser

response = chain.invoke({
    "topic": "machine learning"
})

print("TYPE:", type(response))
print("IS STRING:", isinstance(response, str))
print("VALUE:", response)