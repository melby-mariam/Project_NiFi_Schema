from pathlib import Path
import pdfplumber
from .utils import ensure_dir


def extract_schema_to_markdown(pdf_path: str, markdown_path: str) -> None:
    """
    Read the schema PDF and generate a Markdown file.

    NOTE: This is a SKELETON implementation.
    Later you will improve the extraction logic to:
      - Identify the schema table section
      - Extract field names, types, lengths, rules, etc.
    For now, it just dumps all text into a markdown file with a basic header.
    """
    pdf_path_obj = Path(pdf_path)
    markdown_path_obj = Path(markdown_path)

    ensure_dir(markdown_path_obj.parent.as_posix())

    lines: list[str] = []
    lines.append("# File Schema\n")
    lines.append(f"_Source PDF_: `{pdf_path_obj.name}`\n\n")

    with pdfplumber.open(pdf_path_obj) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            lines.append(text)
            lines.append("\n\n")

    markdown_path_obj.write_text("\n".join(lines), encoding="utf-8")
