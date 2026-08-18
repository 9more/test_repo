from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions

from src.chunker import chunk_text


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

DATA_PATH = Path("data/knowledge_base.md")
CHROMA_PATH = Path("index/chroma")

COLLECTION_NAME = "portfolio"


# ---------------------------------------------------------
# Chroma client
# ---------------------------------------------------------

def create_client():
    """
    Create a persistent Chroma client.

    The database will be stored on disk at CHROMA_PATH.
    """

    CHROMA_PATH.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(
        path=str(CHROMA_PATH)
    )

    return client


# ---------------------------------------------------------
# Embedding function
# ---------------------------------------------------------

def create_embedding_function():
    """
    Create the Sentence Transformer embedding function.

    We use the same embedding model that we used in our
    FAISS implementation.
    """

    embedding_function = (
        embedding_functions
        .SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
    )

    return embedding_function


# ---------------------------------------------------------
# Collection
# ---------------------------------------------------------

def get_collection(client):
    """
    Get or create the portfolio collection.
    """

    embedding_function = create_embedding_function()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    return collection


# ---------------------------------------------------------
# Load knowledge base
# ---------------------------------------------------------

def load_knowledge_base():
    """
    Read the Markdown knowledge base.
    """

    text = DATA_PATH.read_text(
        encoding="utf-8"
    )

    return text


# ---------------------------------------------------------
# Prepare documents
# ---------------------------------------------------------

def prepare_documents():
    """
    Chunk the knowledge base and prepare the data
    required by Chroma.
    """

    text = load_knowledge_base()

    sections = chunk_text(text)

    documents = []
    metadatas = []
    ids = []

    for i, section in enumerate(sections):

        documents.append(
            section["text"]
        )

        metadatas.append(
            {
                "section": section["section"],
                "source": DATA_PATH.name
            }
        )

        ids.append(
            f"chunk_{i}"
        )

    return documents, metadatas, ids


# ---------------------------------------------------------
# Ingestion
# ---------------------------------------------------------

def ingest():
    """
    Read, chunk and store the knowledge base
    in Chroma.
    """

    client = create_client()

    collection = get_collection(client)

    documents, metadatas, ids = prepare_documents()

    collection.upsert(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    print(
        f"Indexed {len(documents)} documents."
    )

    print(
        f"Collection: {COLLECTION_NAME}"
    )

    print(
        f"Total documents in collection: "
        f"{collection.count()}"
    )


# ---------------------------------------------------------
# Retrieval
# ---------------------------------------------------------

def retrieve(query, top_k=3):
    """
    Retrieve the most relevant documents for a query.
    """

    client = create_client()

    collection = get_collection(client)

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results


# ---------------------------------------------------------
# Pretty-print retrieval results
# ---------------------------------------------------------

def print_results(results):
    """
    Display retrieved documents in a readable format.
    """

    documents = results.get("documents", [[]])[0]

    metadatas = results.get("metadatas", [[]])[0]

    distances = results.get("distances", [[]])[0]

    ids = results.get("ids", [[]])[0]

    for i, document in enumerate(documents):

        print("\n" + "-" * 50)

        print(
            f"Result {i + 1}"
        )

        print(
            f"ID: {ids[i]}"
        )

        print(
            f"Distance: {distances[i]}"
        )

        print(
            f"Section: "
            f"{metadatas[i]['section']}"
        )

        print(
            f"Source: "
            f"{metadatas[i]['source']}"
        )

        print("\nDocument:")

        print(document)


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    print("Creating Chroma index...\n")

    ingest()

    print("\nTesting retrieval...\n")

    query = (
        "What classifier was used "
        "for spam detection?"
    )

    results = retrieve(
        query=query,
        top_k=3
    )

    print_results(results)

