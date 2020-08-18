from application import mysql

def get_all_users():
    cursor = get_cursor()
    #cursor.execute("INSERT INTO testinguser (firstname, lastname) VALUES ('yaosheng', 'xu');")
    #con.commit()
    cursor.execute('SELECT * FROM USER;') #get all the data from the user table

    rv = cursor.fetchall()
    # session['user'] = rv[1]
    return rv

#---------------------
# WISHLIST FUNCTIONS |
#---------------------

def add_item_to_wishlist(userid,itemid): #function to add items to wishlist
    if check_if_item_already_exist_in_wishlist(userid,itemid): #check if the item already exist in the wishlist, return if returns true
        return
    else:
        sql = 'INSERT INTO Wishlist(UserID,ItemID) values({},{})'.format(userid,itemid)
        insert_or_delete_database(sql)

def get_the_users_wishlist(id): #function to get the user's wish list
    cursor = get_cursor()
    cursor.execute('SELECT * from Wishlist WHERE UserID = "{}"'.format(id))
    rv = cursor.fetchall()
    if not rv: #check if the tuple is empty, if it is return None
        return None
    else:
        wishlist = get_the_wishlist_items_by_ids(rv)
        return wishlist
    
def delete_item_from_wish_list(userid,itemid):
    sql = 'DELETE FROM Wishlist WHERE UserID={} AND ItemID={}'.format(userid,itemid)
    insert_or_delete_database(sql)

def get_the_wishlist_items_by_ids(list): #function to get the items that is in the wishlist by the item Id
    cursor = get_cursor()
    item_ids = []
    sql = 'SELECT * from Item WHERE '
    for i in list:
        sql =  sql +  'ItemID={}'.format(i[1]) +' OR ' #go through the list of item ids and add it to the SQL
    sql = sql[0:len(sql)-3] #trim the sql to erase the last 'OR'
    cursor.execute(sql)
    list = cursor.fetchall()
    return list #RETURNS a list of Items

def check_if_item_already_exist_in_wishlist(userid,itemid): #function to check if the items already exist in the user's  wishlist
    cursor = get_cursor()
    cursor.execute('SELECT * FROM Wishlist where UserID={} AND ItemID={}'.format(userid,itemid))
    list = cursor.fetchall()
    if list: # if the list is not empty, the item already exist
        return True
    else:
        return False


#-------------------
# HELPER FUNCTIONS |
#-------------------
def insert_or_delete_database(sql): #function to make database insertion or deletion
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def get_cursor(): #return the connection cursor
    connection = mysql.connection
    cursor = connection.cursor()
    return cursor
