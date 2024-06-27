from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    bio = db.Column(db.String(50), nullable=False)

    wishlists = db.relationship('Wishlist', back_populates='user', cascade='all, delete-orphan')

    books = association_proxy('wishlists', 'book',
                               creator=lambda book_obj: Wishlist(book=book_obj))

    def __repr__(self):
        return f'User: {self.username}, email: {self.email}, bio:{self.bio}'

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
class Book(db.Model, SerializerMixin):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    summary = db.Column(db.String(200))
    page_count = db.Column(db.Integer)

    wishlists = db.relationship('Wishlist',back_populates='book', cascade='all, delete-orphan')

    user = association_proxy('wishlists', 'user',
                              creator=lambda user_obj: Wishlist(user=user_obj))

    def __repr__(self):
        return f'Book: {self.title}, Author: {self.author}, Page Count: {self.page_count}, Summary: {self.summary}, Image URL: {self.image}'

class Wishlist(db.Model, SerializerMixin):
    __tablename__ = 'wishlists'

    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))  

    user = db.relationship("User", back_populates='wishlists')
    book = db.relationship('Book', back_populates='wishlists')

    def __repr__(self):
        return f'User: {self.user_id}, Book: {self.book_id}'