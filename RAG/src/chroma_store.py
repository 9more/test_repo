import chromadb


client = chromadb.PersistentClient(
    path="index/chroma"
)
collection = client.get_or_create_collection(
    name="portfolio"
)