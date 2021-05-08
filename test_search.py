from flask_testing import TestCase
from main import app

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

        