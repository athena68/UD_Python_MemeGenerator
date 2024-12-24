import os
import random
import argparse
from src.quote_engine import Ingestor, QuoteModel
from src.meme_generator import MemeGenerator


def generate_meme(image_path=None, body=None, author=None):
    """
    Generate a meme using optional parameters.

    :param image_path: Path to an image file.
    :param body: Quote body text.
    :param author: Quote author.
    :return: Path to the generated meme.
    """
    output_dir = "./tmp"
    meme_generator = MemeGenerator(output_dir)

    # Select a random image if none is provided
    if image_path is None:
        images_path = "./_data/photos/dog/"
        image_path = random.choice([
            os.path.join(images_path, file)
            for file in os.listdir(images_path)
            if file.endswith(('.jpg', '.png'))
        ])

    # Select a random quote if none is provided
    if body is None or author is None:
        quotes_path = "./_data/DogQuotes/"
        all_quote_files = [
            os.path.join(quotes_path, file)
            for file in os.listdir(quotes_path)
            if file.endswith(('.txt', '.csv', '.docx', '.pdf'))
        ]
        quotes = []
        for quote_file in all_quote_files:
            quotes.extend(Ingestor.parse(quote_file))

        random_quote = random.choice(quotes)
        body = random_quote.body
        author = random_quote.author

    # Generate the meme
    meme_path = meme_generator.make_meme(image_path, body, author)
    return meme_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meme Generator CLI")
    parser.add_argument('--path', type=str, help="Path to an image file.")
    parser.add_argument('--body', type=str, help="Quote body text.")
    parser.add_argument('--author', type=str, help="Quote author.")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
