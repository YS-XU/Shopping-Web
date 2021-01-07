import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv('.env')) #finds the .env file


# function to send the email to the user
def send_out_email_after_purchase(purchase_data,receiver_email,invoice_num):
    sender_email = os.environ.get('GMAIL_SENDER')
    password = os.environ.get('GMAIL_PASSWORD') 
    print(sender_email,password)
    total_price = purchase_data['total']
    subtotal = purchase_data['subtotal']
    tax = purchase_data['tax'] 

    message = MIMEMultipart("alternative")
    message["Subject"] = "Thank you for your order. Invoice #: {}".format(invoice_num)
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        Thank you for shopping with us!<br>
        <a href="http://www.realpython.com">Shop with us again!</a> 
        </p>
        <h1>Your Order Summary</h1>
        <p>Subtotal {}</p>
        <p>Tax {}</p>
        <p>Total {}</p>
    </body>
    </html>
    """.format(subtotal,tax,total_price)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
            print(f'Sucessfuly sent to {receiver_email}!')
        except Exception as e:
            print(e)