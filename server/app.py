#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User
# Add your model imports


# Views go here!
class Signup(Resource):
    def post(self):
        data = request.get_json()

        if 'username' not in data:
            return {'error': 'Please enter desired username'}, 422
        user = User(
            email=data['email'],
            username=data['username'],
            bio=data['bio']
        )

        user.password_hash = data['password']

        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict()
        response = make_response(
            user_dict,
            200
        )
        return response

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()

        if user:
            user_dict = user.to_dict()
            response = make_response(
                user_dict,
                200
            )
            return response
        else:
            return {'error': 'Not logged in'}, 401

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        user = User.query.filter_by(username=username).first()

        password = data.get('password')

        try:
            if user.authenticate(password):
                session['user_id'] = user.id
                user_dict = user.to_dict()
                response = make_response(
                    user_dict,
                    200
                )
                return response
        except:
            response = make_response(
                {'error': 'Invalid credentials'},
                401
            )
            return response

class Logout(Resource):
    def delete(self):
        user = User.query.filter(User.id ==session.get('user_id')).first
        if user:
            session['user_id'] = None
            return {'message': 'You have been successfully logged out!'}, 204
        else:
            return {'error': 'No user to logout'}, 401


api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

