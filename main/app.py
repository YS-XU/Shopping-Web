from flask import Flask, render_template
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
mysql = MySQL(app) 

load_dotenv(find_dotenv('.env')) #finds the env file

#set up the database configurations
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASS')
app.config['MYSQL_DB'] = os.getenv('DB')
app.config['MYSQL_PORT'] = int(os.getenv('PORT'))

@app.route('/getdata') #route to test the database
def data():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM testinguser;')
    rv = cur.fetchall()
    return str(rv)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register/")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)