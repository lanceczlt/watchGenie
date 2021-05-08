from flask_testing import TestCase
from main import app

import unittest


class FlaskTestCase(unittest.TestCase):


    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/visualization', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    #  check if content returned if its html/text 
    def test_index_route(self):
        tester = app.test_client(self)
        response = tester.get('/visualization', content_type='html/text')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    #  check if data returned is correct
    def test_index_visualization_html_data(self):
        tester = app.test_client(self)
        response = tester.get('/visualization', content_type='html/text')
        self.assertTrue(b'If not click the link.' in response.data)

    #  check if data returned is correct
    def test_index_visualization_content_data_(self):
        tester = app.test_client(self)
        response = tester.get('/visualization', content_type='application/json')
        self.assertFalse(response.is_json)
        





if __name__ == '__main__':
    unittest.main()