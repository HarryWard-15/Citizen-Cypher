# from flask import Flask, redirect, url_for, render_template, request, flash
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from sqlalchemy.sql import func


# app = Flask(__name__)
# # app.config.from_object(Config) 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:u%MrTo0&4sV4@localhost/citizencypher'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.app_context().push()

# db = SQLAlchemy(app)

# db.drop_all()

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     realname = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(100), nullable=False)

#     def __repr__(self):
#         return '<Name %r' % self.name
    
# db.create_all()


# loggedIn = True

# @app.route('/')
# def home():
#     if loggedIn == False:
#         return redirect(url_for('login'))
#     return render_template('index.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/signup', methods=('POST'))
# def signup():
#     if request.method == 'POST':
#         # test if user exists, if it does then inform user
#         email = request.form.get('email')
#         existing_user = Users.query.filter_by(email=email).first()
#         if existing_user:
#             flash('Email exists in database! You might already have an account. Please log in.')
#             return render_template('signup.html')
        
#         db.session.add(
#             Users(
#             realname = request.form.get('realname'),
#             email = request.form.get('email'),
#             password = request.form.get('password')
#             )
#         )
#         db.session.commit()

#     return render_template('signup.html')

# @app.route('/logout')
# def logout():
#     return render_template('login.html')

# @app.route('/game')
# def game():
#     return render_template('game.html')

# if __name__ == '__main__':
#     app.run(debug=True)