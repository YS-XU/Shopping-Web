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
    sql = 'SELECT * from Wishlist WHERE UserID = "{}"'.format(id)
    cursor.execute(sql)
    rv = cursor.fetchall()
    if not rv: #check if the tuple is empty, if it is return None
        return None
    else:
        wishlist = get_the_wishlist_items_by_ids(rv)
        return wishlist

def get_all_item_ids_from_wishlist(userid,userhome=False): #function to get a list of itemm ids inside the user's wishlist
    sql = 'SELECT ItemID FROM Wishlist WHERE UserID={}'.format(userid) #returns the item ids
    cursor = get_cursor()
    cursor.execute(sql)
    list =   cursor.fetchall()
    if userhome is True: #if the userhome route is calling this function, then just check if list is empty or not and return True or False
        if list:
            return True
        else:
            return False
    else:
        final = []
        for i in list:
            final.append(i[0])
    return tuple(final)

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

#------------------------
# ADD TO CART FUNCTIONS |
#------------------------

def get_item_to_cart(itemid):
    cursor = get_cursor()
    sql = 'SELECT * from Item WHERE '
    for i in itemid:
        sql =  sql +  'ItemID={}'.format(i) +' OR '
    sql = sql[0:len(sql)-3]
    cursor.execute(sql)
    cart = cursor.fetchall()
    return cart

def add_item_to_user_cart(userid, itemid, quantity):
    sql = "INSERT INTO Cart (UserID, ItemID, Quantity) VALUES ({}, {}, {})".format(userid, itemid, quantity)
    insert_or_delete_database(sql)

#def get_item_from_user_cart(userid):
#    cursor = get_cursor()
#    sql = "SELECT ItemID FROM Cart WHERE UserID={}".format(userid)
#    cursor.execute(sql)
#    user_cart = cursor.fetchall()
#    return user_cart

#-------------------
# HELPER FUNCTIONS |
#-------------------
def insert_or_delete_database(sql): #function to make database insertion or deletion
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

def get_cursor(): #return the connection cursor
    connection = mysql.connection
    cursor = connection.cursor()
    return cursor
