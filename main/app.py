from flask import Flask, render_template,request,session,redirect
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv,find_dotenv

app = Flask(__name__)
mysql = MySQL(app)

load_dotenv(find_dotenv('.env')) #finds the .env file

#set up the database configurations
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASS')
app.config['MYSQL_DB'] = os.getenv('DB')
app.config['MYSQL_PORT'] = int(os.getenv('PORT'))

@app.route('/getdata') #route to test the database
def data():
    con = mysql.connection
    cursor = con.cursor()

    #cursor.execute("INSERT INTO testinguser (firstname, lastname) VALUES ('yaosheng', 'xu');")
    #con.commit()
    cursor.execute('SELECT * FROM testinguser;') #get all the data from the user table
    rv = cursor.fetchall()

    return str(rv)

@app.route('/home')
@app.route("/") #route to the home page
def home():
    exist = None
    if 'user' not in session: # if 'user' does not exist in session, then declare with None value
        session['user'] = None
    if session['user'] is not None:
        exist = session['user']
        print(exist)
    return render_template("index.html",user=exist)

@app.route("/userhome/") #route to the home page
def userhome():
    #get the user object from the session
    if 'user' not in session or session['user'] == None: #if the user is not logged in then they don't have access to this page
        return redirect('/')
    else: #if user does exist, get the user's firstname from the session
        user = session.get('user')
    return render_template("user/account.html",user=user)

@app.route("/register/") #route to the register page
def register():
    if session['user'] is not None:
        return redirect('/userhome/')
    return render_template("register.html")

@app.route("/signup/", methods=['POST'])
def signup():
    con = mysql.connection
    cursor = con.cursor()
    if request.method == 'POST':
        email = request.form.get('Email')
        firstname = request.form.get('Firstname')
        lastname = request.form.get('Lastname')
        setPassword = request.form.get('Passwords')

        #Check if the user exist
        if cursor.execute("SELECT * FROM USER WHERE Email LIKE %s", [email]):
            return render_template("error.html")

        #insert new user information into user table
        cursor.execute("INSERT INTO USER (Firstname, Lastname, Email, Passwords) VALUES (%s, %s, %s, %s)",
        (firstname, lastname, email, setPassword))
        con.commit()
        return redirect('/register/')


@app.route("/login/", methods=['POST']) #route to the register page
def login():
    con = mysql.connection
    cursor = con.cursor()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #query the database for user table by the username
        #select * from user where username = 'username'
        #if user does exist, then compare the password
        if cursor.execute("SELECT * FROM USER WHERE Email LIKE %s", [username]):
            if cursor.execute("SELECT * FROM USER WHERE Email = %s AND Passwords = %s", [username, password] ):
                #if the user exist and password matches then login succuess
                session['user'] = cursor.execute("SELECT Firstname FROM USER WHERE Email = %s", [username])
                return redirect('/userhome/')

        return render_template("error.html")


@app.route('/personal/') #route to the user's personal settings page
def personal_details():
    return render_template('user/personaldetails.html')


if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'fdsfsdfdsfsdfdsfsfsdf'
    app.run(debug=True)
