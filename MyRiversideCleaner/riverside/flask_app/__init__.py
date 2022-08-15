from flask import Flask
from flask_mail import Mail, Message
import os
import smtplib
import ssl

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
mail = Mail(app)


app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config["MAIL_USERNAME"] = "support@myriversidecleaner.com"
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")

mail = Mail(app)


app.secret_key = os.environ.get("SECRET_KEY")
