from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingestor for .txt files."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .txt file to extract quotes."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file type: {path}")

        quotes = []
        with open(path, 'r') as file:
            for line in file:
                if '-' in line:
                    body, author = line.strip().split(' - ')
                    quotes.append(QuoteModel(body, author))
        return quotes
