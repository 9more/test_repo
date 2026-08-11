from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "What classifier was used for spam detection?"

documents = [
    "LinearSVC is used as the classification algorithm.",
    "React is used for the frontend.",
    "The weather is sunny today."
]

query_embedding = model.encode([query])
document_embeddings = model.encode(documents)

similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)

for document, score in zip(documents, similarities[0]):
    print(f"{score:.4f} - {document}")