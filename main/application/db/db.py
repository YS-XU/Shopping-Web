from application import mysql
from flask import session

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

#----------------------------
# PROCESS PAYMENT FUNCTIONS |
#----------------------------
def save_invoice(userid,ordernum,date,buyer,street,city,state,zip,country,price): #func to save invoice after payment proccess
    sql = 'INSERT INTO Invoice(UserID,OrderNumber,Dates,Buyer,Street,City,State,Zipcode,Country,Price) VALUES({},"{}","{}","{}","{}","{}","{}","{}","{}","{}");'.format(
    userid,ordernum,date,buyer,street,city,state,zip,country,price
    )
    insert_or_delete_database(sql)

def retrieve_invoice(order): #func to get the invoice info
    cursor = get_cursor();
    cursor.execute('SELECT * FROM Invoice WHERE OrderNumber={};'.format(order))
    order_list = cursor.fetchall()
    print(order_list)
    return order_list

def save_user_credit_card(userid,cc,fullname): #func to save the user's credit card crudentials
    #check if the credit card already exists
    if user_credit_card_exists(userid): # don't do anything if a credit card already exists
        return
    else: # save the user credit card if it does not exist
        sql = 'INSERT INTO Creditcard(UserID,Card,Fullname,Dates,Csc) VALUES({},"{}","{}","{}","{}");'.format(userid,cc[0],fullname,cc[1],cc[2])
        insert_or_delete_database(sql)

def empty_user_cart_after_purchase(userid): #func to empty out the user's cart after purchase
    sql = 'DELETE FROM Cart WHERE UserID={};'.format(userid)
    insert_or_delete_database(sql)

def user_credit_card_exists(userid): #boolean func to check if the user credit card already exists
    sql = 'SELECT * FROM Creditcard WHERE UserID={};'.format(userid)
    cursor = get_cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        return True
    else:
        return False

def get_the_user_submission_invoice(userid,ordernumber):
    cursor = get_cursor()
    #get the items from the user;s CART
    sql = 'SELECT * FROM Invoice WHERE OrderNumber={}'.format(ordernumber)
    cursor.execute(sql)
    invoice = cursor.fetchall()
    items = get_item_to_cart_user(userid)
    data = {
        'invoice':invoice[0],
        'items':items
    }
    empty_user_cart_after_purchase(userid)
    return data


#------------------------
# ADD TO CART FUNCTIONS |
#------------------------

def get_item_to_cart_user(userid):
    cursor = get_cursor()
    #sql = 'SELECT * from Item WHERE '
    sql = "SELECT Item.ItemID, Item, Price, Categories, Subcategories, Image, Quantity FROM Item JOIN Cart ON Item.ItemID = Cart.ItemID WHERE UserID={}".format(userid)
    #for i in itemid:
      #  sql =  sql +  'Item.ItemID={}'.format(i) +' OR '
    #sql = sql[0:len(sql)-3]
    cursor.execute(sql)
    cart = cursor.fetchall()

    new_cart = []
    for price in cart:
        price = list(price)
        price[2] = str(round(float(price[2]) * float(price[6]), 2))
        price = tuple(price)
        new_cart.append(price)

    #print(cart)
    new_cart = tuple(new_cart)
    print(new_cart)
    return new_cart

def get_item_to_cart_guest(itemid, item_quantity):
    cursor = get_cursor()
    sql = 'SELECT * from Item WHERE '
    for i in itemid:
        sql =  sql +  'ItemID={}'.format(i) +' OR '
    sql = sql[0:len(sql)-3]
    cursor.execute(sql)
    cart = cursor.fetchall()

    new_cart = []
    count = 0
    for item in cart:
        item = list(item)
        item.append(item_quantity[count])

        item[2] = str(round(float(item[2]) * float(item[6]), 2))
        item = tuple(item)
        new_cart.append(item)
        count += 1

    new_cart = tuple(new_cart)
    return new_cart

def get_item_from_user_cart(userid):
    cursor = get_cursor()
    cursor.execute("SELECT ItemID FROM Cart WHERE UserID={}".format(userid))
    item_list = []
    for i in cursor.fetchall():
        item_list.append(i[0])

    session['cart'] = tuple(item_list)

def add_item_to_guest_cart(itemid, cart, quantity):
    list_item = list(cart)
    list_item_quantity = list(quantity)
    for i in cart:
        if i == itemid:
            quantity

def add_item_to_user_cart(userid, itemid, quantity):
    print(userid)
    print(itemid)
    if check_if_item_already_exist_in_cart(userid,itemid): #check if the item already exist in the wishlist, return if returns true
        increase_quantity_user(itemid, userid)
    else:
        sql = "INSERT INTO Cart (UserID, ItemID, Quantity) VALUES ({}, {}, {})".format(userid, itemid, quantity)
        insert_or_delete_database(sql)

def increase_quantity_user(itemid, userid):
    cursor = get_cursor()
    cursor.execute("SELECT Quantity FROM Cart WHERE ItemID={} AND UserID={}".format(itemid, userid))
    quantity = cursor.fetchone()
    quantity = list(quantity)
    quantity[0] = str(int(quantity[0] + 1))
    quantity = tuple(quantity)
    sql = "UPDATE Cart SET Quantity={} WHERE ItemID={} AND UserID={}".format(quantity[0], itemid, userid)
    insert_or_delete_database(sql)

def decrease_quantity_user(itemid, userid):
    cursor = get_cursor()
    cursor.execute("SELECT Quantity FROM Cart WHERE ItemID={} AND UserID={}".format(itemid, userid))
    quantity = cursor.fetchone()
    quantity = list(quantity)
    if quantity[0] > 1:
        quantity[0] = str(int(quantity[0] - 1))
    quantity = tuple(quantity)
    sql = "UPDATE Cart SET Quantity={} WHERE ItemID={} AND UserID={}".format(quantity[0], itemid, userid)
    insert_or_delete_database(sql)

def check_if_item_already_exist_in_cart(userid, itemid):
    cursor = get_cursor()
    cursor.execute('SELECT * FROM Cart WHERE UserID={} AND ItemID={}'.format(userid,itemid))
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

def get_cursor(): #return the connection cursor
    connection = mysql.connection
    cursor = connection.cursor()
    return cursor
