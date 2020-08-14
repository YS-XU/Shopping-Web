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
