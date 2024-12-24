from typing import List
from docx import Document
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingestor for .docx files."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .docx file to extract quotes."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file type: {path}")

        quotes = []
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text and '-' in paragraph.text:
                body, author = paragraph.text.split(' - ')
                quotes.append(QuoteModel(body.strip(), author.strip()))
        return quotes
