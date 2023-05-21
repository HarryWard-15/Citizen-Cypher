import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="u%MrTo0&4sV4",
        auth_plugin='mysql_native_password',
        )


def initialise_db(db_obj):
    my_cursor = cnx.cursor()
    my_cursor.execute("DROP DATABASE IF EXISTS citizencypher")
    my_cursor.execute("CREATE DATABASE citizencypher")
    my_cursor.execute("USE citizencypher")

    class User(db_obj.Model):
        __tablename__ = 'user'

        id = db_obj.Column(db_obj.Integer, primary_key=True)
        realname = db_obj.Column(db_obj.String(50), nullable=False)
        email = db_obj.Column(db_obj.String(100), nullable=False, unique=True)
        password = db_obj.Column(db_obj.String(128), nullable=False)

        previous_games = relationship("PreviousGame", backref="user")

        def __repr__(self):
            return '<Name %r>' % self.realname

    class PreviousGame(db_obj.Model):
        __tablename__ = 'previous_game'

        id = db_obj.Column(db_obj.Integer, primary_key=True, nullable=False)
        userId = db_obj.Column(db_obj.Integer, ForeignKey('user.id'), nullable=False)
        causeOfDeath = db_obj.Column(db_obj.String(64), nullable=False)
        daysSurvived = db_obj.Column(db_obj.Integer, nullable=False)

        def __repr__(self):
            return '<PreviousGames %r>' % self.daysSurvived

    class currentGame(db_obj.Model):
        __tablename__ = 'current_game'

        id = db_obj.Column(db_obj.Integer, primary_key=True)
        daysAlive = db_obj.Column(db_obj.Integer, nullable=False)
        happiness = db_obj.Column(db_obj.Integer, nullable=False)
        saturation = db_obj.Column(db_obj.Integer, nullable=False)
        fitness = db_obj.Column(db_obj.Integer, nullable=False)
        sleep = db_obj.Column(db_obj.Integer, nullable=False)


    db_obj.create_all()

    sample_users = [
        User(realname='Sample user A', email='a@a.a', password='a'),
        User(realname='Sample user B', email='b@b.b', password='b')
    ]

    sample_games = [
        PreviousGame(userId=1, causeOfDeath = 'Died because of low Happiness', daysSurvived = 27),
        PreviousGame(userId=1, causeOfDeath = 'Died because of low Saturation', daysSurvived = 16),
        PreviousGame(userId=1, causeOfDeath = 'Died because of low Fitness', daysSurvived = 4),
        PreviousGame(userId=1, causeOfDeath = 'Died because of low Sleep', daysSurvived = 50),

        PreviousGame(userId=2, causeOfDeath = 'Died because of low Happiness', daysSurvived = 25),
        PreviousGame(userId=2, causeOfDeath = 'Died because of low Saturation', daysSurvived = 20),
        PreviousGame(userId=2, causeOfDeath = 'Died because of low Fitness', daysSurvived = 8),
        PreviousGame(userId=2, causeOfDeath = 'Died because of low Sleep', daysSurvived = 34)

    ]

    db_obj.session.add_all(sample_users)
    db_obj.session.add_all(sample_games)
    db_obj.session.commit()

    my_cursor.close()

def create_cursor():
    return_cursor = cnx.cursor()
    return return_cursor