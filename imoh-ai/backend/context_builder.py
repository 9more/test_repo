from knowledge import load_all_knowledge


def build_context(question: str) -> str:
    """
    Build the context supplied to the LLM.

    Currently returns the entire knowledge base.
    Later this will perform semantic retrieval.
    """

    return load_all_knowledge()