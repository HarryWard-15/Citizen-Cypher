from flask import render_template, redirect, url_for, request, session, jsonify
from datetime import datetime
from app import app
from app import db
import connection.sqlconnector as sqlconnector
import requests, json

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
            session['userid'] = account[0]
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
            session['loggedIn'] = True
            session['realname'] = realname
            return redirect(url_for('home'))

    return render_template('signup.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedIn', None)
    session.pop('realname', None)
    return redirect(url_for('home'))

@app.route('/game', methods=['GET','POST'])
def game():
    if request.method == "POST":
        print("successful game data post")
        r = request.get_json()
        print(r)
        print(type(r))

        # json_dict = json.loads(r)

        death_string = "Died because of low " + r["death_stat"]

        days_survived = "Survived " + str(r["days_count"]) + " days"

        print(death_string)
        print(days_survived)

        cursor = sqlconnector.create_cursor()
        ins_query = "INSERT INTO previous_game(userid, causeOfDeath, daysSurvived) VALUES (" + str(session['userid']) + ', "' + death_string + '", ' + str(r["days_count"]) + ")"
        print(ins_query)

        cursor.execute(ins_query)
        cursor.execute("SELECT * FROM previous_game")
        for pg in cursor:
            print(pg)


    return render_template('game.html')

@app.route('/history')
def history():
    cursor = sqlconnector.create_cursor()

    userid = session['userid']

    games = []
    gameid, deathreason, dayssurvived = [], [], []

    query = "SELECT * FROM previous_game WHERE userid = " + str(userid)
    cursor.execute(query)
    game_obj = cursor.fetchall()
    for obj in game_obj:
        games.append(obj)
        gameid.append(obj[0])
        deathreason.append(obj[2])
        dayssurvived.append(obj[3])

    return render_template('history.html', games=games, gameid=gameid, deathreason=deathreason, dayssurvived=dayssurvived)