import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, UserAccount, Item, db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    @app.route('/')
    def index():
        return "hellooh"
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    @app.route('/signup', methods=['POST'])
    def signup():
        body = request.get_json()
        email = body.get('email1', None)
        password = body.get('password1', None)
	# If the email and password are valid, create a new user in the database
        new_user = UserAccount(UserName=email, Password=password, Address="", items="")
        new_user.insert()

        new_user_id = UserAccount.query.filter(UserAccount.UserName == email).all()

        # Return a JSON response with a status code of 201 (Created) and the new user ID
        return jsonify({'userId': new_user_id[0].id}), 200
    @app.route('/login', methods=['POST'])
    def login():
        body = request.get_json()
        email = body.get('email1', None)
        password = body.get('password1', None)
        user_account = UserAccount.query.filter(UserAccount.UserName == email).all()
        if len(user_account) == 0:
            response = {
                "success": False,
                "message": "Login was not successfull"
            }
        elif len(user_account) != 0:
            response = {
                "success": True,
                "message": "logged in successfully",
                "userId": user_account[0].id
            }
        return jsonify(response)
    @app.route('/users/<user_id>/items', methods=['GET'])
    def userItems(user_id):
        user_items = Item.query.filter(Item.user_id == user_id).all()
        items_dict = [items.format() for items in user_items]
        return jsonify(items_dict)
    return app
