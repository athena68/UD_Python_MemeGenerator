from typing import List
from .quote_model import QuoteModel
from .text_ingestor import TextIngestor
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor

class Ingestor:
    """Unified interface to parse any supported file type."""

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file using the appropriate ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"No suitable ingestor found for file: {path}")
