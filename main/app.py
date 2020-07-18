from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app) 

#set up the database configurations
app.config['MYSQL_HOST'] = 'account.cdtpomlk2gyj.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '$hopping1234'
app.config['MYSQL_DB'] = 'shoppingwebapp'
app.config['MYSQL_PORT'] = 3306

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