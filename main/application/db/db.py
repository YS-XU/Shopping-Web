from application import mysql

#function to get all users
def get_all_users():
    con = mysql.connection
    cursor = con.cursor()
    #cursor.execute("INSERT INTO testinguser (firstname, lastname) VALUES ('yaosheng', 'xu');")
    #con.commit()
    cursor.execute('SELECT * FROM USER;') #get all the data from the user table
    rv = cursor.fetchall()
    return rv

#check if user exist in database
def check_if_user_exist(email):
    con = mysql.connection
    cursor = con.cursor()
    if cursor.execute("SELECT * FROM USER WHERE Email LIKE %s", [email]):
        return True
    else:
        return False

# insert new user to database
def insert_new_user(firstname,lastname,email,hashpassword):
    cursor.execute("INSERT INTO USER (Firstname, Lastname, Email, Passwords) VALUES (%s, %s, %s, %s)",
    (firstname, lastname, email, hashPassword))
    con.commit()
    return
