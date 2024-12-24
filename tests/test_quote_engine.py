import unittest
from src.quote_engine import (
    QuoteModel, TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor, Ingestor
)
import os


class TestQuoteEngine(unittest.TestCase):
    """Unit tests for the Quote Engine module."""

    def test_quote_model(self):
        quote = QuoteModel("This is a test", "Author")
        self.assertEqual(str(quote), '"This is a test" - Author')

    def test_text_ingestor(self):
        test_file = "./tests/_data/TestQuotes.txt"
        quotes = TextIngestor.parse(test_file)
        self.assertGreater(len(quotes), 0)
        self.assertEqual(str(quotes[0]), '"Life is short, don’t be late" - Meme Author1')

    def test_csv_ingestor(self):
        test_file = "./tests/_data/TestQuotes.csv"
        quotes = CSVIngestor.parse(test_file)
        self.assertGreater(len(quotes), 0)
        self.assertEqual(str(quotes[0]), '"To be or not to be" - Hamlet')

    def test_docx_ingestor(self):
        test_file = "./tests/_data/TestQuotes.docx"
        quotes = DocxIngestor.parse(test_file)
        self.assertGreater(len(quotes), 0)
        self.assertEqual(str(quotes[0]), '"If you can’t make it good, at least make it look good." - Bill Gates')

    def test_pdf_ingestor(self):
        test_file = "./tests/_data/TestQuotes.pdf"
        quotes = PDFIngestor.parse(test_file)
        self.assertGreater(len(quotes), 0)
        self.assertEqual(str(quotes[0]), '"If you can’t make it good, at least make it look good." - Bill Gates')

    def test_ingestor_unified(self):
        test_file = "./tests/_data/TestQuotes.csv"
        quotes = Ingestor.parse(test_file)
        self.assertGreater(len(quotes), 0)
        self.assertEqual(str(quotes[0]), '"To be or not to be" - Hamlet')

    def test_invalid_file_type(self):
        test_file = "./tests/_data/TestInvalidFile.xyz"
        with self.assertRaises(ValueError):
            Ingestor.parse(test_file)


if __name__ == "__main__":
    unittest.main()
