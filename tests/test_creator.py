import unittest
from app import app


class TestCreatorFeature(unittest.TestCase):
    """Unit tests for the Creator feature in the Flask app."""

    def setUp(self):
        """Set up the test environment."""
        self.client = app.test_client()
        self.client.testing = True

    def test_creator_get(self):
        """Test GET request to the /create route."""
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form', response.data)  # Check if the form is present

    def test_creator_post_valid(self):
        """Test POST request with valid data to the /create route."""
        test_image_url = "https://i.ibb.co/zXHqDVw/test-image.jpg"
        response = self.client.post('/create', data={
            'image_url': test_image_url,
            'body': 'Test Quote',
            'author': 'Tester'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<img', response.data)  # Check if the generated image is displayed

    def test_creator_post_blank_url(self):
        """Test POST request with a blank image URL."""
        response = self.client.post('/create', data={
            'image_url': '',
            'body': 'Test Quote',
            'author': 'Tester'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Image URL is required.', response.data)  # Check for blank URL error message

    def test_creator_post_invalid_url(self):
        """Test POST request with an invalid image URL."""
        response = self.client.post('/create', data={
            'image_url': 'invalid_url',
            'body': 'Test Quote',
            'author': 'Tester'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid URL', response.data)  # Check for invalid URL error

    def test_creator_post_non_image_url(self):
        """Test POST request with a valid URL that is not an image."""
        response = self.client.post('/create', data={
            'image_url': 'http://example.com/',
            'body': 'Test Quote',
            'author': 'Tester'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid image URL. Content is not an image.', response.data)  # Check for non-image content error


if __name__ == '__main__':
    unittest.main()
