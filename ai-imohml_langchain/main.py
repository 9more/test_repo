import os

from huggingface_hub import InferenceClient

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda


client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def call_model(messages):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            {
                "role": "user",
                "content": messages.messages[0].content
            }
        ],
    )

    return response.choices[0].message.content


prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms."
)

model = RunnableLambda(call_model)

chain = prompt | model

response = chain.invoke({
    "topic": "machine learning"
})

print(response)