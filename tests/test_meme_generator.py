import unittest
from src.meme_generator import MemeGenerator
import os


class TestMemeGenerator(unittest.TestCase):
    """Unit tests for the Meme Generator module."""

    def setUp(self):
        """Set up the test environment."""
        self.output_dir = "./tests/_output"
        self.meme_generator = MemeGenerator(self.output_dir)
        self.test_img_path = "./tests/_data/test_image.jpg"

    def test_make_meme(self):
        """Test meme generation."""
        text = "This is a test"
        author = "Tester"
        meme_path = self.meme_generator.make_meme(self.test_img_path, text, author)
        self.assertTrue(os.path.exists(meme_path))
        self.assertTrue(meme_path.endswith(".jpg"))

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)


if __name__ == "__main__":
    unittest.main()
