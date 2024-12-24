from PIL import Image, ImageDraw, ImageFont
import textwrap
import random
import os
from math import floor


class MemeGenerator:
    """A class to generate memes by resizing images and adding captions."""

    def __init__(self, output_dir: str):
        """
        Initialize the MemeGenerator.

        :param output_dir: Directory where the generated memes will be saved.
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """
        Create a meme by resizing the image, adding text, and saving it.

        :param img_path: Path to the input image file.
        :param text: The body of the quote.
        :param author: The author of the quote.
        :param width: The desired width of the image (default 500px).
        :return: Path to the generated meme.
        """
        try:
            # Load and resize the image
            img = Image.open(img_path)
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)
            img = img.resize((width, new_height))

            # Prepare to draw text
            draw = ImageDraw.Draw(img)
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust this path for your system
            font = ImageFont.truetype(font_path, size=20)

            # Combine text and author
            quote = f'"{text}" - {author}'

            # Calculate max characters per line using textbbox
            max_width = width - 20  # Leave some padding
            char_width = draw.textbbox((0, 0), "A", font=font)[2]  # Width of a single character
            max_chars_per_line = floor(max_width / char_width)

            # Wrap the text
            wrapped_text = textwrap.fill(quote, width=max_chars_per_line)

            # Calculate the total text height using textbbox
            total_text_height = 0
            lines = wrapped_text.split('\n')
            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=font)
                line_height = bbox[3] - bbox[1]
                total_text_height += line_height

            # Ensure the text fits vertically within the image
            y_position = random.randint(10, max(10, new_height - total_text_height - 10))

            # Draw each line of wrapped text
            for line in lines:
                draw.text((10, y_position), line, font=font, fill='white')
                bbox = draw.textbbox((0, 0), line, font=font)
                line_height = bbox[3] - bbox[1]
                y_position += line_height

            # Save the meme
            output_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 100000)}.jpg')
            img.save(output_path, "JPEG")
            return output_path

        except Exception as e:
            raise ValueError(f"An error occurred while creating the meme: {e}")
