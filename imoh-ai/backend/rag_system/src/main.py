from pathlib import Path
import faiss
import numpy as np
from pathlib import Path
from src.chunker import chunk_text
from src.embeddings import create_embeddings
from src.vector_store import create_index, save_index

index_path = Path("index/faiss.index")

index_path.parent.mkdir(exist_ok=True)

path = Path("data/knowledge_base.md")
text = path.read_text(encoding="utf-8")
sections = chunk_text(text)
documents = [
    section["text"]
    for section in sections
]
document_embeddings = create_embeddings(documents)

index = create_index(document_embeddings)

index_path = Path("index/faiss.index")

index_path.parent.mkdir(exist_ok=True)

save_index(index, index_path)

print("Number of vectors:", index.ntotal)
print("Index saved to:", index_path)
print("Number of vectors:", index.ntotal)
query = "What classifier was used for spam detection?"
query_embedding = create_embeddings([query])
query_embedding = np.asarray(query_embedding).astype("float32")
faiss.normalize_L2(query_embedding)

distances, indices = index.search(
    query_embedding,
    3
)
for distance, index_number in zip(distances[0], indices[0]):

    print("\n--------------------")

    print("Score:", distance)

    print("Section:", sections[index_number]["section"])

    print("Text:", sections[index_number]["text"])