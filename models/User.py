from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db_obj.Model):
    id = db_obj.Column(db_obj.Integer, primary_key=True)
    realname = db_obj.Column(db_obj.String(50), nullable=False)
    email = db_obj.Column(db_obj.String(100), nullable=False, unique=True)
    password = db_obj.Column(db_obj.String(128), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.realname