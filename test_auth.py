from flask_testing import TestCase
from main import app, create_app 



import unittest






class FlaskTestCase(unittest.TestCase):


    # Ensure that login was set up correctly
    def test_index_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #Tests if the user can log in
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="scescotti0@domainmarket.com",password="awPcsz5IzS6x"), follow_redirects = True)
        print(response.data)
        self.assertTrue(b'You have logged in!' in response.data)

    #Tests if an incorrect password was entered
    def test_incorrect_login_password(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="scescotti0@domainmarket.com",password="aw6x"), follow_redirects = True)
        print(response.data)
        self.assertTrue(b'Incorrect password, please try again.' in response.data)

    #Tests if an incorrect email was used to log in
    def test_incorrect_login_email(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="scescotti0@domainmark.com",password="awPcsz5IzS6x"), follow_redirects = True)
        print(response.data)
        self.assertTrue(b'Email does not exist, please try again.' in response.data)

    #Tests if logout works
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="scescotti0@domainmarket.com",password="awPcsz5IzS6x"), follow_redirects = True)
        response = tester.get('/logout', follow_redirects = True)
        print(response.data)
        self.assertTrue(b'You have logged out!' in response.data)

    

    #Tests if incorrect form of email for signup was used
    def test_incorrect_sign_up_email(self):
        tester = app.test_client(self)
        response = tester.post('/sign_up', data=dict(email="abc",firstName="Edward",lastName="Snowden",gender="Male", password1="1234567",password2="1234567"), follow_redirects = True)
        self.assertTrue(b'Email must be greater than 3 characters.' in response.data)
    
    #Tests if the password used for signup was not long enough
    def test_incorrect_sign_up_password_length(self):
        tester = app.test_client(self)
        response = tester.post('/sign_up', data=dict(email="abc@gmail.com",firstName="Edward",lastName="Snowden",gender="Male", password1="123456",password2="123456"), follow_redirects = True)
        self.assertTrue(b'Password must be at least 7 characters.' in response.data)

    #Tests if the password used for signup does not match the confirmed password
    def test_incorrect_sign_up_password_mismatch(self):
        tester = app.test_client(self)
        response = tester.post('/sign_up', data=dict(email="abc@gmail.com",firstName="Edward",lastName="Snowden",gender="Male", password1="1234567",password2="1234568"), follow_redirects = True)
        self.assertTrue(b'Passwords does not match.' in response.data)
      
    #Tests if the first name for sign up was blank 
    def test_incorrect_sign_up_first_name_blank(self):
        tester = app.test_client(self)
        response = tester.post('/sign_up', data=dict(email="abc@gmail.com",firstName="",lastName="Snowden",gender="Male", password1="1234567",password2="1234567"), follow_redirects = True)
        self.assertTrue(b'Please do not leave first name blank.' in response.data)

    #Tests if the first name for sign up was blank 
    def test_incorrect_sign_up_last_name_blank(self):
        tester = app.test_client(self)
        response = tester.post('/sign_up', data=dict(email="abc@gmail.com",firstName="Edward",lastName="",gender="Male", password1="1234567",password2="1234567"), follow_redirects = True)
        self.assertTrue(b'Please do not leave last name blank.' in response.data)

    #Tests if the gender option for sign up was blank 
    def test_incorrect_sign_up_gender_blank(self):
        tester = app.test_client(self)
        response = tester.post('/sign_up', data=dict(email="abc@gmail.com",firstName="Edward",lastName="Snowden",password1="1234567",password2="1234567"), follow_redirects = True)
        self.assertTrue(b'Please do not leave the gender blank.' in response.data)

    #Tests if signing up works
    def test_valid_sign_up(self):
        tester = app.test_client(self)
        tester.post('/sign_up', data=dict(email="abc@gmail.com",firstName="Edward",lastName="Snowden",password1="1234567",password2="1234567"), follow_redirects = True)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 302)





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

    #tests the need to login for home
    def test_home_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/home', follow_redirects=True)
        self.assertTrue(b'Please login first!' in response.data)
    

    
     



# class TestNotRenderTemplates(TestCase):  

#     render_templates = False   

#     #check if data is returned
#     def test_assert_mytemplate_used(self):
#         response = self.client.get("/template/")
#         self.assert_template_used('login.html')
      


if __name__ == '__main__':
    unittest.main()


