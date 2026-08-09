from document_loader import load_markdown, chunk_text
from embeddings import create_embeddings
from vector_store import VectorStore


# Load document
file_path = "documents/spam_detection.md"

text = load_markdown(file_path)

chunks = chunk_text(text)

print(f"\nDocument contains {len(text)} characters.")
print(f"Created {len(chunks)} chunks.")


# Create embeddings for each chunk
embeddings = create_embeddings(chunks)

print(f"Embedding shape: {embeddings.shape}")


# Create FAISS vector store
store = VectorStore(embeddings)


# Ask a question
query = "What machine learning model was used for spam detection?"

query_embedding = create_embeddings([query])


# Retrieve the most relevant chunks
scores, indices = store.search(
    query_embedding,
    top_k=3,
)


print("\nQuery:")
print(query)

print("\nRelevant chunks:")

for rank, (score, index) in enumerate(
    zip(scores[0], indices[0]),
    start=1,
):

    print("\n" + "=" * 60)
    print(f"RESULT {rank}")
    print(f"Similarity: {float(score):.4f}")
    print("=" * 60)

    print(chunks[index])