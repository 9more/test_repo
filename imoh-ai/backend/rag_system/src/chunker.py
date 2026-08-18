
from src.section_splitter import split_sections
from pathlib import Path

path = Path("data/knowledge_base.md",)
content = path.read_text(encoding="utf-8")

def chunk_section(text):

    paragraphs = text.split("\n\n")

    chunks = []

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if paragraph:
            chunks.append(paragraph)

    return chunks

