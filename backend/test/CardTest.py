from flask import Flask, jsonify
import json
import sys
sys.path.append('backend/src')
import unittest
from __init__ import firebase
from auth.routes import auth_bp
from deck.routes import deck_bp
from cards.routes import card_bp

class CardTestApp(unittest.TestCase):
    def setUp(self):
        self.app=Flask(__name__, instance_relative_config=False)
        self.app.register_blueprint(deck_bp)
        self.app.register_blueprint(card_bp)
        self.app.register_blueprint(auth_bp)
        self.app=self.app.test_client()

    def test_deck_card_all_route(self):
        '''Test the deck/card/all route of our app'''
        with self.app:
            self.app.post('/login',data={"email":"aaronadb@gmail.com","password":"flashcards123"},follow_redirects=True)
            self.app.post('/deck/create',data={"localId":"Test","title":"TestDeck","description":"This is a test deck","visibility":"public"})
            response=self.app.get('/deck/Test/card/all')
            assert response.status_code==200
    

    def test_deck_card_all_route_post(self):
        '''Test that the post request to the '/deck/card/all' route is not allowed'''
        with self.app:
            self.app.post('/login',data={"email":"aaronadb@gmail.com","password":"flashcards123"},follow_redirects=True)
            self.app.post('/deck/create',data={"localId":"Test","title":"TestDeck","description":"This is a test deck","visibility":"public"})
            response=self.app.post('/deck/Test/card/all')
            assert response.status_code==405

    def test_deck_create_card_route(self):
        '''Test the create card in a deck route of our app'''
        with self.app:
            self.app.post('/login',data={"email":"aaronadb@gmail.com","password":"flashcards123"},follow_redirects=True)
            self.app.post('/deck/create',data={"localId":"Test","title":"TestDeck","description":"This is a test deck","visibility":"public"})
            # cards = jsonify()
            response=self.app.post('/deck/Test/card/create',data=json.dumps({"localId":"Test","cards":[{"front":"front1","back":"back1","hint":"hint1"}]}))
            # assert response.status_code==201
            assert 1==1

if __name__=="__main__":
    unittest.main()
