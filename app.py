# Initialising and importing required groundwork for Flask application to run.

from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connection.sqlconnector as sqlconnector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://be09806f63f8e8:f184440b@us-cdbr-east-06.cleardb.net/heroku_0046abaa65d13c4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hellmadsecret'

app.app_context().push()

db = SQLAlchemy(app)

# sqlconnector.initialise_db(db)

import routes.routes as routes

if __name__ == '__main__':
    app.run(debug=False)

