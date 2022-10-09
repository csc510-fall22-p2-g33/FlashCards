#routes.py is a file in deck folder that has all the functions defined that manipulate the deck. All CRUD functions are defined here.
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
try:
    from .. import firebase
except ImportError:
    from __init__ import firebase


deck_bp = Blueprint(
    'deck_bp', __name__
)

db = firebase.database()

#This method is called when we want to fetch one of the decks, we pass deckid of this deck
@deck_bp.route('/deck/<id>', methods = ['GET'])
@cross_origin(supports_credentials=True)
def getdeck(id):
    try:
        deck = db.child("deck").child(id).get()
        return jsonify(
            deck = deck.val(),
            message = 'Fetched deck successfully',
            status = 200
        ), 200
    except Exception as e:
        return jsonify(
            decks = [],
            message = f"An error occurred: {e}",
            status = 400
        ), 400

#This method is called when we want to fetch all of the decks. Here, we check if the user is authenticated, 
#if yes show all the decks made by the user including the ones with private vissibility. if the user is not 
#authenticated then only show decks that have public vissibility.
@deck_bp.route('/deck/all', methods = ['GET'])
@cross_origin(supports_credentials=True)
def getdecks():
    args = request.args
    localId = args and args['localId']
    try:
        if localId:
            user_decks = db.child("deck").order_by_child("userId").equal_to(localId).get()
            decks = []
            for deck in user_decks.each():
                obj = deck.val()
                obj['id'] = deck.key()
                cards = db.child("card").order_by_child("deckId").equal_to(deck.key()).get()
                obj['cards_count'] = len(cards.val())
                decks.append(obj)
                
            return jsonify(
                decks = decks,
                message = 'Fetching decks successfully',
                status = 200
            ), 200
        else:
            alldecks = db.child("deck").order_by_child("visibility").equal_to("public").get()
            d = alldecks.val()
            decks = []
            for deck in alldecks.each():
                obj = deck.val()
                obj['id'] = deck.key()
                cards = db.child("card").order_by_child("deckId").equal_to(deck.key()).get()
                obj['cards_count'] = len(cards.val())
                decks.append(obj)
                
            return jsonify(
                decks = decks,
                message = 'Fetching decks successfully',
                status = 200
            ), 200
    except Exception as e:
        return jsonify(
            decks = [],
            message = f"An error occurred {e}",
            status = 400
        ), 400


#This method is routed when the user requests to create a new deck. To create a new deck, userID, title, description and vissibility are the input required.
@deck_bp.route('/deck/create', methods = ['POST'])
@cross_origin(supports_credentials=True)
def create():
    try:
        data = request.get_json()
        localId = data['localId']
        title = data['title']
        description = data['description']
        visibility = data['visibility']
        
        db.child("deck").push({
            "userId": localId, "title": title, "description": description, "visibility" : visibility
        })
        
        return jsonify(
            message = 'Create Deck Successful',
            status = 201
        ), 201
    except Exception as e:
        return jsonify(
            message = f'Create Deck Failed {e}',
            status = 400
        ), 400

#This method is called when the user requests to update the deck. The deck can be updated in terms of its title, description and vissibility.
@deck_bp.route('/deck/update/<id>', methods = ['PATCH'])
@cross_origin(supports_credentials=True)
def update(id):
    try:
        data = request.get_json()
        deckid = id
        localId = data['localId']
        title = data['title']
        description = data['description']
        visibility = data['visibility']
        
        db.child("deck").order_by_child("deckid").equal_to(f"{localId}_{deckid}").update({
            "deckid":f"{localId}_{deckid}","userId": localId, "title": title, "description": description, "visibility" : visibility
        })
        
        return jsonify(
            message = 'Update Deck Successful',
            status = 201
        ), 201
    except Exception as e:
        return jsonify(
            message = f'Update Deck Failed {e}',
            status = 400
        ), 400
 
#This method is called when the user requests to delete the deck. Only the deckid is required to delete the deck.
@deck_bp.route('/deck/delete/<id>', methods = ['DELETE'])
@cross_origin(supports_credentials=True)
def delete(id):
    try:
        db.child("deck").child(id).remove()
        
        return jsonify(
            message = 'Delete Deck Successful',
            status = 200
        ), 200
    except Exception as e:
        return jsonify(
            message = f'Delete Deck Failed {e}',
            status = 400
        ), 400
