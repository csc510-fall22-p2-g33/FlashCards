from flask import Flask
import sys
sys.path.append('backend/src')
import unittest
from __init__ import firebase
from auth.routes import auth_bp
from deck.routes import deck_bp
from cards.routes import card_bp

class AuthTestApp(unittest.TestCase):
    def setUp(self):
        self.app=Flask(__name__, instance_relative_config=False)
        self.app.register_blueprint(auth_bp)
        self.app=self.app.test_client()

    def test_index_get_route(self):
        '''Test the index route of our app'''
        response=self.app.get('/')
        assert response.status_code==200
    
    def test_index_post(self):
        '''Test that the post request to the index route is not allowed'''
        response=self.app.post('/')
        assert response.status_code==405

    def test_signup_route_registered_user(self):
        '''Test the signup route of our app with a registered user'''
        response=self.app.post('/signup', data= {"email":"aaronadb@gmail.com","password":"flashcards123"})
        assert response.status_code==400
        
    def test_signup_route_unregistered_user_invalid_email(self):
        '''Test the signup route of our app with an unregistered user using an invalid email address'''
        response=self.app.post('/signup',data=dict(email='test@gmail.com',password='password123'))
        assert response.status_code==400
        
    def test_signup_route_registered_user(self):
        '''Test the signup route of our app with a registered user'''
        #This has been tested manually, programming this test is not possible right now, because the functionality for deleting an account has not been implemented as yet
        pass
        
    def test_login_route_registered_user(self):
        '''Test the login route of our app with an already registered user'''
        #This has been tested manually, programming this test is not possible right now, because the functionality for deleting an account has not been implemented as yet
        pass
        
    def test_login_route_wrong_password(self):
        '''Test the login route of our app with a registered user with a wrong password'''
        response=self.app.post('/login',data=dict(email='aaronadb@gmail.com',password='flashcards'))
        assert response.status_code==400
        
    def test_login_route_unregistered_user(self):
        '''Test the login route of our app with an unregistered user'''
        response=self.app.post('/login',data=dict(email='aarondiasbarreto@gmail.com',password='flashcards123'))
        assert response.status_code==400
        

if __name__=="__main__":
    unittest.main()




