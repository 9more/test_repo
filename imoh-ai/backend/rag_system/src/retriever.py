from sklearn.metrics.pairwise import cosine_similarity


def retrieve(query_embedding, document_embeddings, documents, top_k=3):

    similarities = cosine_similarity(
        query_embedding,
        document_embeddings
    )[0]

    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices[:top_k]:
        results.append({
            "document": documents[index],
            "score": similarities[index]
        })

    return results