from flask_testing import TestCase
from main import app

import unittest


class FlaskTestCase(unittest.TestCase):


    # Ensure that flask was set up correctly
    def test_index_rec(self):
        tester = app.test_client(self)
        response = tester.get('/recommendation', content_type='html/text')
        self.assertEqual(response.status_code, 308)
    
    #tests the need to login for recommendation
    def test_recommendation_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/recommendation', follow_redirects=True)
        self.assertTrue(b'Please login first!' in response.data)

    #  check if content returned if its html
    # def test_index_route_rec(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/recommendation', content_type='html/text')
    #     self.assertEqual(response, "text/html")