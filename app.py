# Initialising and importing required groundwork for Flask application to run.

from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import connection.sqlconnector as sqlconnector
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

app.app_context().push()

db = SQLAlchemy(app)

# sqlconnector.initialise_db(db)

import routes.routes as routes

if __name__ == '__main__':
    app.run(debug=False)

