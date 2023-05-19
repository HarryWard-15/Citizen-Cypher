from flask import render_template, flash, redirect, url_for, request, flash, session
from datetime import datetime
from app import app
from app import db
import sqlconnector 

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    my_cursor = sqlconnector.create_cursor()
    if request.method == 'POST':
        print("successful post")
        email = request.form['email']
        password = request.form['password']

        query = "SELECT * FROM user WHERE email = \"" + email + "\" AND password = \"" + password + "\""
        
        my_cursor.execute(query)
        account = my_cursor.fetchone()
        
        if account:
            session['loggedIn'] = True
            session['realname'] = account[1]
            return redirect(url_for('home'))
        else:
            msg = "Please check credentials!"
        
    return render_template('login.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    my_cursor = sqlconnector.create_cursor()
    if request.method == "POST":
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
    session.pop('loggedIn', None)
    session.pop('realname', None)
    return redirect(url_for('login'))

@app.route('/game')
def game():
    return render_template('game.html')