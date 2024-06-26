#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource
import datetime

# Local imports
from config import app, db, api
from models import User, Book, Wishlist
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
        session['user_id'] = user.id

        db.session.add(user)
        db.session.commit()
        user_dict = user.to_dict()
        response = make_response(
            user_dict,
            200
        )
        return response

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        user = User.query.filter_by(username=username).first()
        user_dict = user.to_dict()
        print(user_dict)

        password = data.get('password')
        if user.authenticate(password):
            session['user_id'] = user.id
            response = make_response(
                user_dict,
                200
            )
            return response
        else:
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

# class CheckSession(Resource):
#     def get(self):
#         user = User.query.filter(User.id == session.get('user_id')).first()

#         if user:
#             user_dict = user.to_dict()
#             response = make_response(
#                 user_dict,
#                 200
#             )
#             return response
#         else:
#             return {'error': 'Not logged in'}, 401

@app.before_request
def check_if_logged_in():
    if 'user_id' not in session or not session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 401

class Books(Resource):
    def get(self):
        books = [book.to_dict(rules=('-wishlists',)) for book in Book.query.all()]
        response = make_response(
            books,
            200
        )
        return response

    def post(self):
        data = request.get_json()
        new_book = Book(
            title = data['title'],
            author = data['author'],
            image = data['image'],
            summary = data['summary'],
            page_count = data['page_count']
        )

        db.session.add(new_book)
        db.session.commit()

        new_book_dict = new_book.to_dict(rules=('-wishlists',))

        response = make_response(
            jsonify(new_book_dict),
            200
        )
        return response

class BooksByID(Resource):
    def get(self,id):
        book_dict = Book.query.filter_by(id=id).first().to_dict(rules=('-wishlists',))
        response = make_response(
            book_dict,
            200
        )
        return response

    def patch(self,id):
        book = Book.query.filter(Book.id==id).first()
        for attr in request.form:
            setattr(book, attr, request.form[attr])

        db.session.add(book)
        db.session.commit()

        book_dict = book.to_dict(rules=('-wishlists',))

        response = make_response(
            book_dict,
            200
        )

        return response

    def delete(self, id):
        book = Book.query.filter_by(id=id).first()
        db.session.delete(book)
        db.session.commit

        return make_response(
            {'message':'Book successfully deleted'},
            200
        )

class UserByID(Resource):
    def get(self,id):
        user = User.query.filter_by(id=id).first()

        if user:
            user_dict = user.to_dict(rules=('-wishlists',))
            response = make_response(
                user_dict,
                200
            )
            return response

    def patch(self,id):
        user = User.query.filter(User.id == id).first()

        if user:
             for attr in request.form:
                setattr(user, attr, request.form[attr])

                db.session.add(user)
                db.session.commit()

                user_dict = user.to_dict(rules=('-wishlists',))

                response = make_response(
                    user_dict,
                    200
                )
                return response

    def delete(self,id):
        user = User.query.filter(User.id==id).first()

        if user:
            db.session.delete(user)
            db.session.commit()

            return make_response(
                {'message': 'Successfully deleted'},
                200
            )

class WishlistByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()

        wishlist_books = user.wishlists
        user_wishlist = []
        for wishlist in wishlist_books:
            book = wishlist.book
            user_wishlist.append(book.to_dict(rules=('-wishlists',)))

        response = make_response(
            jsonify(user_wishlist),
            200
        )
        return response


class AddToWishlist(Resource):
     def post(self):
        data = request.get_json()
        new_wishlist= Wishlist(
            user_id=data['user_id'],
            book_id=data['book_id']
         )
        db.session.add(new_wishlist)
        db.session.commit()

        new_wishlist_dict = new_wishlist.to_dict(rules=('-book.wishlists',))

        response = make_response(
            new_wishlist_dict,
            200
         )

        return response



api.add_resource(Signup, '/signup')
# api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Books, '/books')
api.add_resource(BooksByID, '/books/<int:id>')
api.add_resource(UserByID, '/user_by_id/<int:id>')
api.add_resource(WishlistByID, '/wishlist_by_id/<int:id>')
api.add_resource(AddToWishlist, '/add_to_wishlist')



if __name__ == '__main__':
    app.run(port=5555, debug=True)

