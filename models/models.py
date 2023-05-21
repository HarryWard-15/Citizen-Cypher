from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    realname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))

    previous_games = relationship("PreviousGame", backref="User")

    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class PreviousGame(db.Model):

    __tablename__ = "previous_game"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    causeOfDeath = db.Column(db.String(128), nullable=False)
    daysSurvived = db.Column(db.Integer, nullable=False)


    def __repr__(self):
            return "<PreviousGames %r>" % self.daysSurvived