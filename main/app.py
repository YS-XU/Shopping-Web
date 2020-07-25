from flask import Flask, render_template,request,session
from flask_mysqldb import MySQL
import os
<<<<<<< HEAD
from dotenv import load_dotenv,find_dotenv
=======
from dotenv import load_dotenv, find_dotenv
>>>>>>> f2d522d6f8e93644fcd272791c41a7932ad1b11b

app = Flask(__name__)
mysql = MySQL(app)

load_dotenv(find_dotenv('.env')) #finds the .env file

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
    cur.execute('SELECT * FROM testinguser;') #get all the data from the user table
    rv = cur.fetchall()
    return str(rv)

@app.route("/") #route to the home page
def home():
    exist = None
    if session['user'] is not None:
        exist = session['user']
    return render_template("index.html",user=exist)

@app.route("/userhome/") #route to the home page
def userhome():
    return render_template("userhome.html")


@app.route("/register/") #route to the register page
def register():
    if session['user'] is not None:
        return redirect('userhome')
    return render_template("register.html")

@app.route("/login/",methods=['POST']) #route to the register page
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #query the database for user table by the username
        #select * from user where username = 'username'
        #if user does exist, then compare the password

        #if the user exist and password matches then...
        session['user'] = username

        print(username,password)


        return redirect('userhome',name=name)






if __name__ == "__main__":
    app.run(debug=True)
