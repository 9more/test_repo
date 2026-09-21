from pathlib import Path


def split_sections(text):

    raw_sections = text.split("## ")

    sections = []

    for section in raw_sections[1:]:

        heading, content = section.split("\n", 1)

        sections.append({
            "section": heading.strip(),
            "text": content.strip()
        })

    return sections

if __name__ == "__main__":

    path = Path(
        "data/knowledge_base.md"
    )

    text = path.read_text(
        encoding="utf-8"
    )

    sections = split_sections(text)

    for section in sections:

        print("\n" + "=" * 50)

        print(
            "SECTION:",
            section["section"]
        )

        print("=" * 50)

        print(section["text"])