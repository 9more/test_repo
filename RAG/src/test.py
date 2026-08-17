from pathlib import Path
from src.vector_store import load_index


path="index/faiss.index"
print(load_index(path).ntotal)
