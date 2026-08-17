from pathlib import Path
import faiss
from src.embeddings import create_embeddings
from src.vector_store import load_index, load_metadata


INDEX_PATH = Path("index/faiss.index")
METADATA_PATH = Path("index/metadata.pkl")


def retrieve(query, top_k=3):

    index = load_index(INDEX_PATH)

    metadata = load_metadata(METADATA_PATH)

    query_embedding = create_embeddings([query])

    query_embedding = query_embedding.astype("float32")

    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_number in zip(
        distances[0],
        indices[0]
    ):

        results.append({
            "score": float(distance),
            "section": metadata[index_number]["section"],
            "text": metadata[index_number]["text"]
        })

    return results

if __name__ == "__main__":

    query = "What classifier was used for spam detection?"

    results = retrieve(query)

    for result in results:

        print("\n--------------------")
        print("Score:", result["score"])
        print("Section:", result["section"])
        print("Text:", result["text"])