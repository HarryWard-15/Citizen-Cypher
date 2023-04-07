from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

loggedIn = True

@app.route('/')
def home():
    if loggedIn == False:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)