class QuoteModel:
    """A model to encapsulate a quote with a body and author."""

    def __init__(self, body: str, author: str):
        """Initialize the QuoteModel object."""
        self.body = body
        self.author = author

    def __str__(self):
        """String representation of the QuoteModel."""
        return f'"{self.body}" - {self.author}'
