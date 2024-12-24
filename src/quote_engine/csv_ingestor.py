import pandas as pd
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel

class CSVIngestor(IngestorInterface):
    """Ingestor for .csv files."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .csv file to extract quotes."""
        if not cls.can_ingest(path):
            raise ValueError(f"Cannot ingest file type: {path}")

        quotes = []
        df = pd.read_csv(path)
        for _, row in df.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))
        return quotes
