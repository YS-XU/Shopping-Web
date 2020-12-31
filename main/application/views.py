from flask import render_template,request,session,redirect,flash,jsonify,url_for
import random
from passlib.hash import sha256_crypt
import os
from application import app, mysql
from flask_mysqldb import MySQL
from dotenv import load_dotenv,find_dotenv
from application.db.db import * #import everything from the db module
from application.email.email import send_out_email_after_purchase

load_dotenv(find_dotenv('.env')) #finds the .env file

@app.route('/getdata') #route to test the database
def data():
    con = mysql.connection
    cursor = con.cursor()
    #cursor.execute("INSERT INTO testinguser (firstname, lastname) VALUES ('yaosheng', 'xu');")
    #con.commit()
    cursor.execute('SELECT * FROM USER;') #get all the data from the user table

    rv = cursor.fetchall()
    # session['user'] = rv[1]
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

    if 'cart' and 'quantity' not in session:
        session['cart'] = None
        session['quantity'] = None

    return render_template("index.html",user=exist)

@app.route("/userhome/") #route to the account home page
def userhome():
    #get the user object from the session
    if not check_if_user_is_logged_in(): #if the user is not logged in then they don't have access to this page
        return redirect('/')
    else: #if user does exist, get the user's firstname from the session
        user = session.get('user')
        wishlist = get_all_item_ids_from_wishlist(session.get('id'),True) #get the wishlist from the database to determine if the user has one
        print(wishlist)
    return render_template("user/account.html",user=user,wishlist=wishlist)


@app.route("/signout/") #route to sign out the account
def signout():
    session.clear()
    print(session)
    return redirect("/")

@app.route("/register/") #route to the register page
def register():
    try:
        if session['user'] is not None: #if user exist, then go to the user's account page
            return redirect('/userhome/')
    except KeyError as e:
        print(e)
    return render_template("register.html")

@app.route("/signup/", methods=['POST']) #route to sign up the account
def signup():
    if request.method == 'POST':
        con = mysql.connection
        cursor = con.cursor()
        email = request.form.get('Email')
        firstname = request.form.get('Firstname')
        lastname = request.form.get('Lastname')
        setPassword = request.form.get('Passwords')
        hashPassword = sha256_crypt.hash(setPassword)
        #Check if the user exist
        if cursor.execute("SELECT * FROM USER WHERE Email LIKE %s", [email]):
            existError = "Email already exist"
            return render_template("register.html", existError=existError)

        #insert new user information into user table
        cursor.execute("INSERT INTO USER (Firstname, Lastname, Email, Passwords) VALUES (%s, %s, %s, %s)",
        (firstname, lastname, email, hashPassword))
        con.commit()
        return redirect('/register/')

@app.route("/login/", methods=['POST']) #route to the register page
def login():
    if request.method == 'POST':
        con = mysql.connection
        cursor = con.cursor()
        username = request.form.get('username')
        password = request.form.get('password')
        #query the database for user table by the username
        #select * from user where username = 'username'
        #if user does exist, then compare the password
        if cursor.execute("SELECT * FROM USER WHERE Email LIKE %s", [username]):
            rv = cursor.fetchone()
            if sha256_crypt.verify(password, rv[4]):
                #if the user exist and password matches then login succuess
                session['id'] = rv[0]
                session['user'] = rv[1]
                session['email'] = rv[3]
                session['password'] = rv[4]
                return redirect('/userhome/')
            else:
                loginError = "Enter the valid Email or Password"
        else:
            loginError = "Enter the valid Email or Password"
        return render_template("register.html", loginError=loginError)

#----------------------------
#  USER SETTINGS HANDLERS   |
#----------------------------
@app.route('/personal/') #route to the user's personal settings page
def personal_details():
    #get the user object from the session
    if 'user' not in session or session['user'] == None: #if the user is not logged in then they don't have access to this page
        return redirect('/')
    return render_template('user/personaldetails.html')

@app.route('/change_personal_detail/', methods=['POST']) #route to change personal detail
def change_personal_detail():

    if request.method == 'POST':
        con = mysql.connection
        cursor = con.cursor()
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        if firstname:
            cursor.execute("UPDATE USER SET Firstname = %s WHERE Email = %s", (firstname, session['email']))
            session['user'] = firstname

        if lastname:
            cursor.execute("UPDATE USER SET Lastname = %s WHERE Email = %s", (lastname, session['email']))

        con.commit()

    return redirect('/personal/')

@app.route('/change_password/', methods=['POST']) #route to change password
def change_password():
    if request.method == 'POST':
        con = mysql.connection
        cursor = con.cursor()

        currentPass = request.form.get('currentpass')
        newPassword = request.form.get('newpassword')
        hashNewPassword = sha256_crypt.hash(newPassword)

        if sha256_crypt.verify(currentPass, session['password']):
            cursor.execute("UPDATE USER SET Passwords = %s WHERE Email = %s", (hashNewPassword, session['email']))
        con.commit()
    return redirect('/userhome/')

@app.route('/payment-methods/') #route to the user's payment page
def payment_methods():
    #get the user object from the session
    if 'user' not in session or session['user'] == None: #if the user is not logged in then they don't have access to this page
        return redirect('/')
    return render_template('user/paymentmethod.html')

#----------------------------
# ITEMS WEBPAGES HANDLERS   |
#----------------------------
# All route to access Clothing
@app.route('/items/clothing/allClothing/')
def items_clothing():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Categories = 'clothing'")
    item = cursor.fetchall()

    return render_template('item/clothing/allClothing.html',item=item,wishlist=wishlist)

@app.route('/items/clothing/bottom/') #route to the user to access clothing bottom
def items_bottom():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'bottom'")
    item = cursor.fetchall()

    return render_template('item/clothing/bottom.html',item=item,wishlist=wishlist)

@app.route('/items/clothing/dresses/') #route to the user to access clothing dresses
def items_dresses():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'dresses'")
    item = cursor.fetchall()

    return render_template('item/clothing/dresses.html',item=item,wishlist=wishlist)

@app.route('/items/clothing/suits/') #route to the user to access suits
def items_suits():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'suits'")
    item = cursor.fetchall()

    return render_template('item/clothing/suits.html',item=item,wishlist=wishlist)

@app.route('/items/clothing/tops/') #route to the user to access tops
def items_tops():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'top'")
    item = cursor.fetchall()

    return render_template('item/clothing/tops.html',item=item,wishlist=wishlist)

# All route to access Footwear
@app.route('/items/footwear/allFootwear/')
def items_footwear():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Categories = 'footwear'")
    item = cursor.fetchall()

    return render_template('item/footwear/allFootwear.html',item=item,wishlist=wishlist)

@app.route('/items/footwear/sneakers/') #route to the user to access sneakers
def items_sneakers():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'sneakers'")
    item = cursor.fetchall()

    return render_template('item/footwear/sneakers.html',item=item,wishlist=wishlist)

@app.route('/items/footwear/sandles/') #route to the user to access Sandles
def items_sandles():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'sandles'")
    item = cursor.fetchall()

    return render_template('item/footwear/sandles.html',item=item,wishlist=wishlist)

@app.route('/items/footwear/slippers/') #route to the user to access Slippers
def items_slippers():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'slippers'")
    item = cursor.fetchall()

    return render_template('item/footwear/slippers.html',item=item,wishlist=wishlist)

# All route to Accessories
@app.route('/items/accessories/allAccessories/')
def items_accessories():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Categories = 'accessories'")
    item = cursor.fetchall()

    return render_template('item/accessories/allAccessories.html',item=item,wishlist=wishlist)

@app.route('/items/accessories/watches/') #route to the user to access watches
def items_watches():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'watches'")
    item = cursor.fetchall()

    return render_template('item/accessories/watches.html',item=item,wishlist=wishlist)

@app.route('/items/accessories/sunglasses/') #route to the user to access watches
def items_sunglasses():
    wishlist = []
    if check_if_user_is_logged_in():
        wishlist = get_all_item_ids_from_wishlist(session['id'])
    con = mysql.connection
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Item WHERE Subcategories = 'sunglasses'")
    item = cursor.fetchall()

    return render_template('item/accessories/sunglasses.html',item=item,wishlist=wishlist)

#----------------------------
#     WISHLIST HANDLERS     |
#----------------------------
@app.route('/user/wishlist/') #route to the wishlist, ONLY logged in user can access their wishlist
def wishlist_view():
    if check_if_user_is_logged_in():
        wishlist = get_the_users_wishlist(int(session['id'])) #get the list of the user's wishlist, pass in the users id
        print(session['id'])
        return render_template('user/wishlist.html',wishlist=wishlist)
    return redirect('/register/')

@app.route('/user/wishlist/<category>/<subcategory>/<int:id>') #route to add the item to wishlist
def add_to_wishlist(category,subcategory,id): #pass in the cat,and subcat, to redirect to the right page, and id reference item
    if check_if_user_is_logged_in():
        add_item_to_wishlist(session['id'],id) #pass in the user id and the item id
        flash('You addded an item to your wishlist!','success')
        return redirect('/items/{}/{}'.format(category,subcategory))
    return '<h1>401- Unauthorized- Access is Denied</h1>', 401 #if user is not signed in, they don't have access to this route

@app.route('/user/wishlist/delete/<int:id>') #route to delete an item from the user's wishlist, pass in the item id
def delete_from_wishlist(id):
    if check_if_user_is_logged_in(): #check if the user is logged in
        delete_item_from_wish_list(session['id'],id) #pass in the user id and the item id
        flash('You removed an item from your wishlist!','warning')
        return redirect('/user/wishlist/')
    return '<h1>401- Unauthorized- Access is Denied</h1>', 401 #if user is not signed in, they don't have access to this route


#----------------------------
# PROCESS PAYMENT HANDLERS  |
#----------------------------
@app.route('/shopping/checkout/',methods=['POST','GET']) #route for checking out, payment info, and shipping info before proccesing payment
def shopping_checkout_page():
    try:
        if session.get('proccessing') is False: #if proccessing is false, it means that the purchase is already been processed --> avoids click backs
            return redirect(url_for('shoppingcart'))
    except Exception:
        return redirect(url_for('shoppingcart'))

    if request.method == 'GET':
        session['purchase_data'] = {
            'total':request.args.get('total'),
            'subtotal':request.args.get('subtotal'),
            'tax':request.args.get('taxes'),
        }
        print(session)
        
        if session.get('cart'):
            if check_if_user_is_logged_in():
                cart = get_item_to_cart_user(session['id'])
                print(cart)
            else:
                cart = get_item_to_cart_guest(session['cart'], session['quantity'])
                print(cart)
        else:
            cart = None
        
        total = request.args.get('total')
        subtotal = request.args.get('subtotal')
        taxes = request.args.get('taxes')       
        return render_template('testinginvoice.html', cart=cart, subtotal=subtotal, taxes = taxes, total=total)
    elif request.method == 'POST':
        return '<h1>405 Method Now Allowed</h1>',405

@app.route('/processpayment/',methods=['POST']) #set the session proccessing to true, then redirect to the checkout page
def save_key_to_proccess():
    session['proccessing'] = True #setting the processing to true
    return redirect(url_for('process_the_payment'),code=307) #redirecting to the process payment handler, passing in 307 code to reserve the DATA from FORM

@app.route('/shopping/checkout/submit',methods=['POST','GET']) #route to handle the payment proccess
def process_the_payment():
    if request.method == 'POST':
        # CREDIT CARD INFO FROM WEBPAGE
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        csc = request.form.get('csc')
        date = request.form.get('date')
        cardnumber = request.form.get('cardnumber')

        #SHIPPING INFO FROM WEBPAGE
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.getlist('state')[0]
        zipcode = request.form.get('zipcode')
        country = request.form.get('country')

        order = "%.9d" % random.randint(0,9999999999) #generate a random 10 digit invoice #

        #validate to see if the user is a member or guest
        if check_if_user_is_logged_in():
            cc = [cardnumber,date,csc]  # create a list with the cc information inside
            save_user_credit_card(session.get('id'),cc,'{} {}'.format(firstname,lastname)) #save the user's credit card information -- pass in user id and cc list
            save_invoice(session.get('id'),order,date,'{} {}'.format(firstname,lastname),street,city,state,zipcode,country,session.get('purchase_data')['total']) #save the user's order in record
            info = get_the_user_submission_invoice(session.get('id'),order) #get the users order
            session['info'] = info #store the invoice info into the session
            return redirect(url_for('show_user_invoice'),code=302)#redirect to the invoice page, passing in the order number
        else:
            items = get_list_of_items_based_on_ids(session.get('cart'),True)
            save_invoice(100,order,date,'{} {}'.format(firstname,lastname),street,city,state,zipcode,country,session.get('purchase_data')['total']) #save the user's order in record
            invoice = get_guest_submission_invoice(order)
            session['info'] = {'invoice':invoice,'items': items}
            return redirect(url_for('show_user_invoice'),code=302)
    elif request.method == 'GET':
        return '<h1>405 Method Now Allowed</h1>',405 #pass in not allowed method content and 405 status code

@app.route('/paymentproccess/complete/invoices/') #handler for showing the invoice page with data
def show_user_invoice():
    try:
        info = session['info']
        purchase_data = session['purchase_data']
        print('purchase data',purchase_data)
        #send the email to the user after they have purchased
        try:
            send_out_email_after_purchase(purchase_data,session['email'])
        except Exception as e:
            print(e)
        finish_processing()
    except Exception:
        return redirect(url_for('shoppingcart'))
    return render_template('invoice.html',info=info['invoice'],items=info['items'],purchase=purchase_data)


def finish_processing():#func to change the proccessing to False and delete the info after payment is processed
    try:
        session['proccessing'] = False
        del session['info']
        del session['purchase_data']
        del session['cart']
    except KeyError:
        return

#----------------------------
#   ADD TO CART HANDLERS    |
#----------------------------
@app.route('/addtocart/<category>/<subcategory>/<int:id>') #route to add the item to the cart
def add_to_cart(category, subcategory, id):
    if session.get('cart'):
        quantity_item = list(session['quantity'])
        list_item = list(session['cart'])
        if id in session['cart']:
            index = list_item.index(id)
            quantity_item[index] = quantity_item[index] + 1
        else:
            list_item.append(id)
            quantity_item.append(1)
    else:
        list_item = [id]
        quantity_item = [1]

    if check_if_user_is_logged_in():
        add_item_to_user_cart(session['id'], id, "1")
    print(list_item)
    print(quantity_item)
    session['cart'] = tuple(list_item)
    session['quantity'] = tuple(quantity_item)
    print(session['cart'])
    return redirect('/items/{}/{}'.format(category, subcategory))

@app.route("/shoppingcart/")
def shoppingcart():
    #con = mysql.connection
    #cursor = con.cursor()
    subtotal = 0
    session['proccessing'] = True
    print(session)
    if check_if_user_is_logged_in():
        get_item_from_user_cart(session['id'])

    if session.get('cart'):
        if check_if_user_is_logged_in():
            cart = get_item_to_cart_user(session['id'])
            print(cart)
        else:
            cart = get_item_to_cart_guest(session['cart'], session['quantity'])
            print(cart)
        for price in cart:
            subtotal = round(subtotal + float(price[2]), 2)
    else:
        cart = None

    taxes = round(subtotal * 0.068, 2)
    total = str(round(subtotal + taxes, 2))

    taxes = str(taxes)
    subtotal = str(subtotal)
   # print(cart)
    return render_template("shoppingcart.html", cart=cart, subtotal=subtotal, taxes = taxes, total=total)

@app.route("/increase_quantity/<int:id>")
def increase_quantity(id):
    if check_if_user_is_logged_in():
        increase_quantity_user(id, session['id'])
    else:
        quantity_item = list(session['quantity'])
        index = session['cart'].index(id)
        quantity_item[index] += 1
        session['quantity'] = tuple(quantity_item)

    return redirect('/shoppingcart/')

@app.route("/decrease_quantity/<int:id>")
def decrease_quantity(id):
    if check_if_user_is_logged_in():
        decrease_quantity_user(id, session['id'])
    else:
        quantity_item = list(session['quantity'])
        index = session['cart'].index(id)
        if quantity_item[index] > 1:
            quantity_item[index] -= 1
        session['quantity'] = tuple(quantity_item)
    return redirect('/shoppingcart/')

def check_if_user_is_logged_in(): #function to check if the user is logged in
    try:
        if 'user' in session and session['user'] is not None:
            return True
    except KeyError: #catch if there is a KeyError, there is an error that means that the 'user' does not exist
        return False
    return False
