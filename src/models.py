from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    name = db.Column(db.String, Unique =True, nullable=False)
    atmosphere = db.Column(db.String, Unique =False, nullable=False)
    livable = db.Column(db.String, Unique =False, nullable=False)
    add_to_fav = db.Column(db.Integer, db.ForeignKey("favorites.item"))

class Animals(db.Model):
    name = db.Column(db.String, Unique =True, nullable=False)
    species = db.Column(db.String, Unique =False, nullable=False)
    diet = db.Column(db.String, Unique =False, nullable=False)

class Character(db.Model):
    name = db.Column(db.String, Unique =True, nullable=False)
    origin = db.Column(db.String, Unique =False, nullable=False)
    height = db.Column(db.String, Unique =False, nullable=False)
    add_to_fav = db.Column(db.Integer, db.ForeignKey("favorites.item"))

class Favorites(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item = db.Column(db.String, Unique = False, nullable=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Integer, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("post.id"))

class Messages(db.Model):
     inbox = db.Column(db.String(500), unique=False, nullable=True)
     time_stamp = db.Column(db.Integer, unique=False, nullable=True)
     sender = db.Column(db.String(25), unique=False, nullable=True)
     recepient = db.Column(db.String(25), unique=False, nullable=True)

class List (db.Model):
     friend_id = db.Column(db.String(25), unique=True, nullable=False)
     friend_image = db.Column(nullable=True)
   
    