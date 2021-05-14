from flask_testing import TestCase
from main import app

import unittest


class FlaskTestCase(unittest.TestCase):


    # Ensure that flask was set up correctly
    def test_index_movie_info(self):
        tester = app.test_client(self)
        response = tester.get('/movie_info', content_type='html/text')
        self.assertEqual(response.status_code, 308)

    #  check if content returned if its html
    def test_index_movie_info_content(self):
        tester = app.test_client(self)
        response = tester.get('/movie_info', content_type='html/text')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
    
    #tests the need to login for movie_info
    def test_movie_info_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/movie_info', follow_redirects=True)
        self.assertTrue(b'Please login first!' in response.data)