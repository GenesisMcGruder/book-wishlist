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
        new_user = User(
            email=data['email'],
            username=data['username'],
            bio=data['bio']
        )

        new_user.password_hash = data['password']
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id

        new_user_dict = new_user.to_dict()
        response = make_response(
            new_user_dict,
            200
        )
        return response

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        user = User.query.filter_by(username=username).first()
        user_dict = user.to_dict()

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
    def delete(self, id):
        user = User.query.filter(User.id ==session.get('user_id')).first
        if user:
            session['user_id'] = None
            return {'message': 'You have been successfully logged out!'}, 204
        else:
            return {'error': 'No user to logout'}, 401

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        
        if user_id:
            user = User.query.filter(User.id == user_id).first()
            if user:
                user_dict = user.to_dict()
                response = make_response(
                    user_dict,
                    200
                )
                return response
            else:
                    return {'error': "User not found"}, 404
        else:
            return {'error': 'Not logged in'}, 401

class Books(Resource):
    def get(self):
        if not session['user_id']:
            return {'error': 'Not logged in'}
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
        data = request.get_json()
        book = Book.query.filter(Book.id==id).first()
        for attr in data:
            setattr(book, attr, data[attr])

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


class WishlistByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()

        if not user:
            return make_response(jsonify(message="User not found"), 404)

        wishlist_books = user.wishlists
        user_wishlist = []
        for wishlist in wishlist_books:
            book = wishlist.book
            if wishlist.book:
                user_wishlist.append(book.to_dict(rules=('-wishlists',)))

        response = make_response(
            jsonify(user_wishlist),
            200
        )
        return response


class AddToWishlist(Resource):
     def post(self):
        data = request.get_json()
        user_id=data.get('user_id')
        book_id=data.get('book_id')

        existing_book = Wishlist.query.filter_by(user_id=user_id, book_id=book_id).first()

        if existing_book:
            return {'error': f"Book {book_id} already exists in wishlist"}, 400
        else:
            new_wishlist= Wishlist(
                user_id=user_id,
                book_id=book_id
            )

        db.session.add(new_wishlist)
        db.session.commit()

        new_wishlist_dict = new_wishlist.to_dict(rules=('-book.wishlists',))

        response = make_response(
            new_wishlist_dict,
            200
         )

        return response

class DeleteFromWishlist(Resource):
       def delete(self,user_id, book_id):
        wishlist_entry = Wishlist.query.filter_by(user_id = user_id, book_id = book_id).first()

        if not wishlist_entry:
            return {'message': 'Book not found in user wishlist'}

        db.session.delete(wishlist_entry)
        db.session.commit()

        return make_response(
            {'message':f'Book {book_id} deleted from user {user_id} wishlist'},
            200
        )


class UpdateUser(Resource):
    def patch(self,id):
        user = User.query.filter(User.id == id).first()
        data = request.get_json()

        if not user:
            return {'message': 'User not found'}, 404

        if user:
             for attr in data:
                if attr == 'password':
                    user.password_hash = data['password']
                    setattr(user,attr, 'password' )
                else:
                    setattr(user, attr, data[attr])

        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict(rules=('-wishlists',))

        response = make_response(
            user_dict,
            200
        )
        return response



api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout/<int:id>')
api.add_resource(Books, '/books')
api.add_resource(BooksByID, '/books/<int:id>')
api.add_resource(WishlistByID, '/wishlist_by_id/<int:id>')
api.add_resource(AddToWishlist, '/add_to_wishlist')
api.add_resource(UpdateUser, '/update_user/<int:id>')
api.add_resource(DeleteFromWishlist, '/delete_from_wishlist/<int:user_id>/<int:book_id>')



if __name__ == '__main__':
    app.run(port=5555, debug=True)

