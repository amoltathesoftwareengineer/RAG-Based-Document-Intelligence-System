
import pytest

from text_splitter import split_text
from document_loader import extract_text_from_pdf


def test_split_text_returns_chunks():
    chunks = split_text("A" * 2000, chunk_size=800, overlap=150)

    assert len(chunks) > 1
    assert all(chunks)


def test_split_text_empty_input():
    assert split_text("") == []
    assert split_text("   ") == []


def test_split_text_invalid_overlap():
    with pytest.raises(ValueError):
        split_text("example", chunk_size=10, overlap=10)


def test_split_text_invalid_chunk_size():
    with pytest.raises(ValueError):
        split_text("example", chunk_size=0)


def test_pdf_file_not_found():
    with pytest.raises(FileNotFoundError):
        extract_text_from_pdf("missing_test_document.pdf")


def test_non_pdf_file_rejected(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Example text", encoding="utf-8")

    with pytest.raises(ValueError):
        extract_text_from_pdf(file_path)
