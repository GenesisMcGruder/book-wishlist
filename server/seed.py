#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random
import datetime

# Remote library imports
from faker import Faker
import requests

# Local imports
from app import app
from models import db, User, Book, Wishlist

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print ('Deleteing data...')
        User.query.delete()
        Book.query.delete()
        Wishlist.query.delete()
        print("Starting seed...")
        users = []
        usernames = []

        for i in range(10):
            username = fake.first_name()
            counter = 1
            while username in usernames:
                username = f"{fake.first_name()}{counter}"
                counter += 1
            usernames.append(username)

            user = User(
                email= fake.unique.email(),
                username=username,
                bio=fake.paragraph(nb_sentences=2)
            )

            user.password_hash = user.username + 'password'

            users.append(user)

        db.session.add_all(users)
        db.session.commit() 


        books = []
        for i in range(15):
            summary = fake.paragraph(nb_sentences=2)

            response = requests.get('https://picsum.photos/200')
            image = response.url

            book = Book(
                title = fake.sentence(),
                author = fake.name(),
                summary = summary,
                page_count = randint(1, 1000),
                image = image
            )

            books.append(book)

        db.session.add_all(books)
        db.session.commit()

        
        num_wishlist = 15
        wishlists = []
        for i in range(num_wishlist):

            wishlist = Wishlist(
                # date_added = datetime.datetime.now(),
                user_id = randint(1,10),
                book_id = randint(1,15)
            )

            wishlists.append(wishlist)

            db.session.add(wishlist)
            db.session.commit()
    


        print('Complete!')
        # Seed code goes here!
