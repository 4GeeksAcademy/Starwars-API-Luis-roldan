from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    favorites = db.relationship("Favorites", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username":self.username
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dimension = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    population = db.Column(db.String(100), nullable=False)
    favorites = db.relationship("Favorites", back_populates="planet")



class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eye_color = db.Column(db.String(100), nullable=False)
    height = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    favorites = db.relationship("Favorites", back_populates="character")



class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="favorites")
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="favorites")
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character", back_populates="favorites")




