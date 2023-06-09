from flask import render_template, redirect, url_for, request, session
from datetime import datetime
from app import app
from app import db
import connection.sqlconnector as sqlconnector
import requests, json
from models.models import User, PreviousGame

##################
### DECORATORS ###
##################


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


#########################################################
# Login method: create SQL cursor, check if POST request
# then search database for matching credentials entered.
# fetch it into cursor, and if an account exists, assign
# session variables and redirect to home.
# Display a message on screen if credentials invalid.
#########################################################
@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user is None or not user.check_password(request.form["password"]):
            msg = "Please check credentials!"


        session["loggedIn"] = True
        session["userid"] = user.id
        session["realname"] = user.realname
        return redirect(url_for("home"))


    return render_template("login.html", msg=msg)


#############################################################
# Signup method: create SQL cursor, check if POST request
# then search database for matching email entered.
# If email exists in database, display message on screen.
# If not, insert a new row into User table with credentials.
# Assign session variables and redirect to home.
#############################################################
@app.route("/signup", methods=["GET", "POST"])
def signup():
    msg = ""
    if request.method == "POST":
        realname = request.form["realname"]
        email = request.form["email"]
        password = request.form["password"]

        account = User.query.filter_by(email=email).first()

        # query = 'SELECT * FROM user WHERE email = "' + email + '"'

        # my_cursor.execute(query)
        # account = my_cursor.fetchone()

        if account:
            msg = "This email already exists in the database!"
        else:
            password = User.set_password(password, password)
            user = User(realname=realname, email=email, password=password)
            db.session.add(user)
            db.session.commit()

            msg = "Account successfully registered!"
            session['userid'] = user.id
            session["loggedIn"] = True
            session["realname"] = realname
            return redirect(url_for("home"))

    return render_template("signup.html", msg=msg)


#############################################################
# Logout method: pop user session variables, redirect to home
#############################################################
@app.route("/logout")
def logout():
    session.pop("userid", None)
    session.pop("loggedIn", None)
    session.pop("realname", None)
    return redirect(url_for("home"))

###############################################################
# Game method: game logic happens clientside; this route exists
# to receive JSON game data from client and insert into database
###############################################################
@app.route("/game", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        print("successful game data post")
        r = request.get_json()
        print(r)

        death_string = "Died because of low " + r["death_stat"]

        userId = session["userid"]
        daysSurvived = r["days_count"]

        prevGame = PreviousGame(userId=userId, causeOfDeath=death_string, daysSurvived=daysSurvived)
        db.session.add(prevGame)
        db.session.commit()

        print(prevGame)

    return render_template("game.html")


####################################################################
# History method: create SQL cursor, retrieve entries from database
# and pass them to html for Jinja to format on page.
###################################################################
@app.route("/history")
def history():

    userid = session["userid"]

    games = []
    gameid, deathreason, dayssurvived = [], [], []

    gameList = PreviousGame.query.filter_by(userId=userid).all()

    for obj in gameList:
        games.append(obj.id)
        gameid.append(obj.userId)
        deathreason.append(obj.causeOfDeath)
        dayssurvived.append(obj.daysSurvived)

    return render_template(
        "history.html",
        games=games,
        gameid=gameid,
        deathreason=deathreason,
        dayssurvived=dayssurvived,
    )
