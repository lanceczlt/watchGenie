from flask_testing import TestCase
from main import app, create_app

import unittest


class FlaskTestCase(unittest.TestCase):


    # Ensure that flask was set up correctly
    def test_index_search(self):
        tester = app.test_client(self)
        response = tester.get('/search', content_type='html/text')
        self.assertEqual(response.status_code, 302)


    #  check if content returned if its html
    def test_index_search_content(self):
        tester = app.test_client(self)
        response = tester.get('/search', content_type='html/text')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    #  check if data returned is correct
    def test_index_search_content_data(self):
        tester = app.test_client(self)
        response = tester.get('/search', content_type='html/text')
        self.assertTrue(b'If not click the link.' in response.data)

    #tests the need to login for search
    def test_search_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/search', follow_redirects=True)
        self.assertTrue(b'Please login first!' in response.data)

    #tests the need to login for result
    def test_recommendation_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/result', follow_redirects=True)
        self.assertTrue(b'Please login first!' in response.data)

        