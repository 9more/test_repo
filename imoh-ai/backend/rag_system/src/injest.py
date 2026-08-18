from pathlib import Path

from src.section_splitter import split_sections
from src.chunker import chunk_section


path = Path("data/knowledge_base.md")

text = path.read_text(
    encoding="utf-8"
)

sections = split_sections(text)

all_chunks = []

for section in sections:

    chunks = chunk_section(
        section["text"]
    )

    for chunk in chunks:

        all_chunks.append({
            "section": section["section"],
            "text": chunk
        })


print("\nNumber of sections:", len(sections))

print(
    "Number of chunks:",
    len(all_chunks)
)

print("\nFinal chunks:\n")

for i, chunk in enumerate(all_chunks):

    print("=" * 50)

    print("Chunk:", i)

    print("Section:", chunk["section"])

    print("Text:", chunk["text"])