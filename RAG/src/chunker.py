def chunk_text(text):
    sections = []
    current_section = None
    current_content = []

    for line in text.splitlines():

        if line.startswith("## "):
            if current_section and current_content:
                sections.append({
                    "section": current_section,
                    "text": "\n".join(current_content).strip()
                })

            current_section = line.replace("## ", "").strip()
            current_content = []

        elif current_section:
            current_content.append(line)

    if current_section and current_content:
        sections.append({
            "section": current_section,
            "text": "\n".join(current_content).strip()
        })

    return sections