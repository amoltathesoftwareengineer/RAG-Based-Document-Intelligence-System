
from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    reader = PdfReader(str(path))

    if reader.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported.")

    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        if text.strip():
            pages.append(text.strip())

    extracted_text = "\n\n".join(pages)

    if not extracted_text:
        raise ValueError(
            "No readable text found. The PDF may be scanned or empty."
        )

    return extracted_text
