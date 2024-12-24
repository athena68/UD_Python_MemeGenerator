# Meme Generator Project

This project is a **Meme Generator** application that allows users to create memes dynamically. The application can generate random memes or accept custom user input to create personalized memes.

## Features

- Generate random memes with quotes and images.
- Create custom memes using an image URL, quote body, and author.
- Command-line interface for generating memes.
- Web interface powered by Flask for an intuitive user experience.

## Setup Instructions

1. Clone the repository:

   ```bash
    git clone https://github.com/your-repo/meme-generator.git
    cd meme-generator
   ```

2. Create and activate a virtual environment:

```bash
 python3 -m venv env
 source env/bin/activate  # On Windows: env\Scripts\activate
 Install dependencies:
```

3. Install dependencies

```bash
pip install -r requirements.txt
Run the application:
```

4. Command-Line Interface:

```bash
python main.py
```

5. Flask Web App:

```bash
python app.py
```

## Project Structure

- app.py: Flask web app to generate memes.
- main.py: Command-line tool for generating memes.
- src/quote_engine/: Classes for ingesting and parsing quotes from various file formats.
- src/meme_generator/: Meme generation logic.
- tests/: Unit tests for the application.

## Example Usage

### Command-Line Tool

Generate a random meme:

```bash
python main.py
```

Generate a custom meme:

```bash
python main.py --path ./src/\_data/photos/dog/xander_1.jpg --body "Code like a pro." --author "Coder"
```

### Web App

1. Start the Flask server:

```bash
python app.py
```

2. Open http://127.0.0.1:5000/ in your browser.
3. Use the random generator or custom meme form.

## Dependencies

- Flask
- Pillow
- Pandas
- Python-Docx

## **What’s Next?**

- Consider deploying the Flask app to a platform like Heroku or AWS.
