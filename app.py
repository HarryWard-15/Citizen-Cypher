from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connection.sqlconnector as sqlconnector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:u%MrTo0&4sV4@localhost/citizencypher'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hellmadsecret'

app.app_context().push()

db = SQLAlchemy(app)
sqlconnector.initialise_db(db)

import routes.routes as routes

if __name__ == '__main__':
    app.run(debug=False)