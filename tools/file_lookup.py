from pathlib import Path
from langchain.tools import tool

# Project folder मधील sample_data.txt file चा path
DATA_FILE = Path(__file__).resolve().parent.parent / "sample_data.txt"


@tool
def file_lookup(query: str) -> str:
    """Search for information in the project's sample_data.txt file."""

    try:
        if not DATA_FILE.exists():
            return "Sorry, the sample_data.txt file was not found."

        content = DATA_FILE.read_text(encoding="utf-8")

        matching_lines = [
            line for line in content.splitlines()
            if query.lower() in line.lower()
        ]

        if matching_lines:
            return "\n".join(matching_lines)

        return f"No information found for: {query}"

    except Exception:
        return "Sorry, an error occurred while searching the file."
