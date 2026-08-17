from pathlib import Path

from src.chunker import chunk_text
from src.embeddings import create_embeddings
from src.vector_store import create_index, save_index, save_metadata


DATA_PATH = Path("data/knowledge_base.md")
INDEX_PATH = Path("index/faiss.index")
METADATA_PATH = Path("index/metadata.pkl")


def ingest():

    text = DATA_PATH.read_text(encoding="utf-8")

    sections = chunk_text(text)

    documents = [
        section["text"]
        for section in sections
    ]

    embeddings = create_embeddings(documents)

    index = create_index(embeddings)

    INDEX_PATH.parent.mkdir(exist_ok=True)

    save_index(index, INDEX_PATH)

    save_metadata(sections, METADATA_PATH)

    print(f"Indexed {len(documents)} documents.")
    print(f"Saved index to {INDEX_PATH}")
    print(f"Saved metadata to {METADATA_PATH}")


if __name__ == "__main__":
    ingest()