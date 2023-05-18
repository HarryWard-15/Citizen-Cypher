from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, MetaData
from datetime import datetime
from flask_migrate import Migrate
import mysql.connector

PYTHONUNBUFFERED=0

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:u%MrTo0&4sV4@localhost/citizencypher'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hellmadsecret'

app.app_context().push()

db = SQLAlchemy(app)
md = MetaData()

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="u%MrTo0&4sV4",
    auth_plugin='mysql_native_password',
    )

my_cursor = cnx.cursor()
my_cursor.execute("DROP DATABASE IF EXISTS citizencypher")
my_cursor.execute("CREATE DATABASE citizencypher")
my_cursor.execute("USE citizencypher")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    realname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.realname
    
db.create_all()

my_cursor.execute("INSERT INTO user(realname, email, password) VALUES ('a a', 'a@a.a', 'a')")
my_cursor.execute("SELECT * FROM user")
for ud in my_cursor:
    print(ud)

my_cursor.close()

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        print("successful post")
        my_cursor = cnx.cursor()

        email = request.form['email']
        password = request.form['password']

        query = "SELECT * FROM user WHERE email = \"" + email + "\" AND password = \"" + password + "\""
        
        my_cursor.execute(query)
        account = my_cursor.fetchone()
        
        if account:
            session['loggedIn'] = True
            session['realname'] = account[1]
            session['email'] = account[2]
            return redirect(url_for('home'))
        else:
            msg = "Please check credentials!"
        
    return render_template('login.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == "POST":
        my_cursor = cnx.cursor()

        realname = request.form['realname']
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT * FROM user WHERE email = \"" + email + "\""
        
        my_cursor.execute(query)
        account = my_cursor.fetchone()
        
        if account:
            msg = 'This email already exists in the database!'
        else:
            ins_query = "INSERT INTO user(realname, email, password) VALUES (\'" + realname + "\', \'" + email + "\', \'" + password + "\')"
            
            my_cursor.execute(ins_query)
            my_cursor.execute("SELECT * FROM user")
            for ud in my_cursor:
                print(ud)
            
            msg = "Account successfully registered!"
    return render_template('signup.html', msg=msg)

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)