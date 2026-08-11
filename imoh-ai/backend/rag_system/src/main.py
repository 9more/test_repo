from src.chunker import chunk_text
from src.embeddings import create_embeddings
from src.retriever import retrieve


with open("data/knowledge_base.md", "r") as file:
    text = file.read()


chunks = chunk_text(text)

document_embeddings = create_embeddings(chunks)


query = "What classifier was used for spam detection?"

query_embedding = create_embeddings([query])


results = retrieve(
    query_embedding,
    document_embeddings,
    chunks,
    top_k=3
)


print("\nQUESTION:")
print(query)


print("\nRETRIEVED DOCUMENTS:")

for result in results:
    print("\n--------------------")
    print("Score:", result["score"])
    print(result["document"])