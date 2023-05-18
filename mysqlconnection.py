import mysql.connector

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


