import subprocess
import os
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class PDFIngestor(IngestorInterface):
    """Ingestor for .pdf files."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .pdf file to extract quotes."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file type: {path}")

        temp_txt = f"{path}.txt"
        try:
            subprocess.run(['pdftotext', path, temp_txt], check=True)
            with open(temp_txt, 'r') as file:
                quotes = [
                    QuoteModel(*line.strip().split(' - '))
                    for line in file if '-' in line
                ]
        finally:
            if os.path.exists(temp_txt):
                os.remove(temp_txt)

        return quotes
