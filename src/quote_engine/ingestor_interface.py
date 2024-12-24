from abc import ABC, abstractmethod
from typing import List
from .quote_model import QuoteModel  # Ensure this path matches your file structure

class IngestorInterface(ABC):
    """Abstract Base Class for all file ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file type is supported."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given file and return a list of QuoteModel instances."""
        pass
