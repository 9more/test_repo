from pathlib import Path


# ============================================
# Paths
# ============================================

BASE_DIR = Path(__file__).resolve().parent

KNOWLEDGE_DIR = BASE_DIR / "knowledge"
PROJECTS_DIR = KNOWLEDGE_DIR / "projects"


# ============================================
# Internal Helper
# ============================================

def _read_markdown(path: Path) -> str:
    """
    Read a markdown file.
    Returns an empty string if the file cannot be read.
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except (FileNotFoundError, OSError):
        return ""


# ============================================
# Personal Knowledge
# ============================================

def load_profile() -> str:
    return _read_markdown(KNOWLEDGE_DIR / "profile.md")


def load_skills() -> str:
    return _read_markdown(KNOWLEDGE_DIR / "skills.md")


def load_experience() -> str:
    return _read_markdown(KNOWLEDGE_DIR / "experience.md")


def load_education() -> str:
    return _read_markdown(KNOWLEDGE_DIR / "education.md")


# ============================================
# Projects
# ============================================

def load_project(project_name: str) -> str:
    """
    Load a single project.

    Examples:
        load_project("Spam Detection")
        load_project("spam_detection")
        load_project("spam detection")
    """

    filename = (
        project_name
        .strip()
        .lower()
        .replace(" ", "_")
    )

    return _read_markdown(PROJECTS_DIR / f"{filename}.md")


def load_all_projects() -> str:
    """
    Load every project article.
    """

    projects = []

    for file in sorted(PROJECTS_DIR.glob("*.md")):
        projects.append(_read_markdown(file))

    return "\n\n".join(projects)


# ============================================
# Complete Knowledge Base
# ============================================

def load_all_knowledge() -> str:
    """
    Load the complete knowledge base.
    """

    sections = [
        load_profile(),
        load_skills(),
        load_experience(),
        load_education(),
        load_all_projects()
    ]

    return "\n\n".join(
        section
        for section in sections
        if section.strip()
    )
    
def list_projects() -> list[str]:
    """
    Return the names of all available projects.
    """

    return [
        file.stem
        for file in sorted(PROJECTS_DIR.glob("*.md"))
    ]