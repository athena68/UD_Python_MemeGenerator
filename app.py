import random
import os
import requests
from flask import Flask, render_template, request, redirect
from src.quote_engine import Ingestor
from src.meme_generator import MemeGenerator

app = Flask(__name__)

# Directory configurations
meme_output_dir = "./static/memes"
meme_generator = MemeGenerator(meme_output_dir)

# Preload images and quotes
images_path = "./_data/photos/dog/"
quotes_path = "./_data/DogQuotes/"

images = [
    os.path.join(images_path, file)
    for file in os.listdir(images_path)
    if file.endswith(('.jpg', '.png'))
]

quote_files = [
    os.path.join(quotes_path, file)
    for file in os.listdir(quotes_path)
    if file.endswith(('.txt', '.csv', '.docx', '.pdf'))
]


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Select a random image
    img = random.choice(images)

    # Select a random quote
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))
    quote = random.choice(quotes)

    # Generate meme
    path = meme_generator.make_meme(img, quote.body, quote.author)
    print(f"Generated meme path: {path}")
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """Display the meme creation form."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a custom meme from user input."""
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    temp_img_path = None

    try:
        if not image_url:
            return render_template('meme_form.html', error="Image URL is required.")

        # Fetch the image using requests
        response = requests.get(image_url, stream=True, allow_redirects=True)

        # Validate the response and ensure it's an image
        if response.status_code != 200:
            return render_template('meme_form.html', error="Invalid image URL. Unable to fetch the image.")
        if 'image' not in response.headers.get('Content-Type', ''):
            return render_template('meme_form.html', error="Invalid image URL. Content is not an image.")

        # Save the image locally
        temp_img_path = f"./static/{random.randint(0, 1000000)}.jpg"
        with open(temp_img_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        # Generate meme
        path = meme_generator.make_meme(temp_img_path, body, author)
        return render_template('meme.html', path=path)

    except Exception as e:
        return render_template('meme_form.html', error=f"Error: {e}")

    finally:
        # Clean up the temporary image file
        if temp_img_path and os.path.exists(temp_img_path):
            os.remove(temp_img_path)


if __name__ == "__main__":
    app.run(debug=True)
