from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
# app.config.from_object(Config) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:u%MrTo0&4sV4@localhost/citizencypher'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r' % self.name



loggedIn = True

@app.route('/')
def home():
    if loggedIn == False:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)