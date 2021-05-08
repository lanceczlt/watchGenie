# from flask import Flask, current_app
# import pytest
# import json

# from main import app
# from website import auth

# with app.app_context():
#     print (current_app.name)
    
# # def inc(x):
# #     return x + 1

# # def test_answer():
# #     assert inc(4) == 5
 

# def test_login():
#     auth.login()
#     client = app.test_client()
#     url = '/login'
    
#     # mock_request_headers ={
#     #     ''


#     # }
#     response = client.get(url)
#     assertTrue()
    
    
# #     response.get_data() == b"LET'S MAKE MAGIC HAPPEN "
# #     assert response.status_code == 200
# # with app.test_request_context():
# #     test_login()



# def test_login_user():
#     auth.login()
#     client = app.test_client()
#     url = '/login'

#     response = client.post(url)
#     assert response.get_data() == b'You have logged in!'

from flask_testing import TestCase
from main import app, create_app 


import unittest


class FlaskTestCase(unittest.TestCase):


    # Ensure that login was set up correctly
    def test_index_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that home was set up correctly
    def test_index_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    # Ensure that logout was set up correctly
    def test_index_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    # Ensure that signup was set up correctly
    def test_index_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    #  check if content returned if its html
    def test_index_login_content(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

    #  check if data returned is correct
    def test_index_login_content_data(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'WATCH GENIE' in response.data)

    #  check if data returned is correct
    def test_index_signup_content_data(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertTrue(b'404 Not Found' in response.data)

    #  check if data returned is correct
    def test_index_logout_content_data(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type='html/text')
        self.assertTrue(b'If not click the link.' in response.data)
    

    
     



# class TestNotRenderTemplates(TestCase):  

#     render_templates = False   

#     #check if data is returned
#     def test_assert_mytemplate_used(self):
#         response = self.client.get("/template/")
#         self.assert_template_used('login.html')
      


if __name__ == '__main__':
    unittest.main()


