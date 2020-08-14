from flask import Flask
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv,find_dotenv


load_dotenv(find_dotenv('.env')) #finds the .env file

app = Flask(__name__) #inits flask inistance

mysql = MySQL(app) #inits the mysql instance


#set up the database configurations
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PASS')
app.config['MYSQL_DB'] = os.getenv('DB')
app.config['MYSQL_PORT'] = int(os.getenv('PORT'))
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from application import views #import all of the routes into the application
