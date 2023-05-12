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

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

