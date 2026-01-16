from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(15), unique=False, nullable=False)

# foreign key to favs
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

# relationships
    favorites.id = relationship('Favorites', back_populates = 'user.id')
    planet = relationship('Planet', back_populates = 'user')
    animals = relationship('Animals', back_populates = 'user')
    character = relationship('Character', back_populates = 'user')
    posts = relationship('Post', back_populates = 'post')
    messages = relationship('Messages', back_populates = 'messages')



    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_id": self.user_id
            #do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), Unique = False, nullable=True)
  


# foreign key to favs
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# relationships
    user.id = relationship('User', back_populates = 'favorites.id')
    planet= relationship('Planet', back_populates = 'favorites')
    animals = relationship('Animals', back_populates = 'favorites')
    character = relationship('Character', back_populates = 'favorites')

class Planet(db.Model):
    __tablename__ = 'planet'

    name = db.Column(db.String, Unique =True, nullable=False)
    atmosphere = db.Column(db.String, Unique =False, nullable=False)
    livable = db.Column(db.String, Unique =False, nullable=False)

# Foreign Keys for user & favorites connection
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

# relationships
    user.id = relationships('User', back_populates = 'planet')
    favorites.id = relationships('Favorites', back_populates = 'planet')

class Animals(db.Model):
    __tablename__ = 'animals'
    name = db.Column(db.String, Unique =True, nullable=False)
    species = db.Column(db.String, Unique =False, nullable=False)
    diet = db.Column(db.String, Unique =False, nullable=False)

# foreign keys for user & favorites
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

#relationships
    user.id = relationships('User', back_populates = 'animals')
    favorites.id = relationships('Favorites', back_populates = 'animals')

class Character(db.Model):
    __tablename__ = 'character'

    name = db.Column(db.String, Unique =True, nullable=False)
    origin = db.Column(db.String, Unique =False, nullable=False)
    height = db.Column(db.String, Unique =False, nullable=False)

# foreign keys for user & favorites
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

#relationships
    user.id = relationships('User', back_populates = 'character')
    favorites.id = relationships('Favorites', back_populates = 'character')

class Post(db.Model):
     __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Integer, unique=False, nullable=False)

# foreign keys for user & favorites
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

# relationships
    user.id = relationships('User', back_populates = 'post')
    favorites.id = relationships('Favorites', back_populates = 'post')

class Messages(db.Model):
    __tablename__ = 'messages'
     inbox = db.Column(db.String, unique=False, nullable=True)
     time_stamp = db.Column(db.Integer, unique=False, nullable=True)
     sender = db.Column(db.String, unique=False, nullable=True)
     recipient = db.Column(db.String, unique=False, nullable=True)

# foreign keys for user
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

# relationships
     user.id = relationships('User', back_populates = 'messages')


class List (db.Model):
     friend_id = db.Column(db.String, unique=True, nullable=False)
     friend_image = db.Column(nullable=True)
   

