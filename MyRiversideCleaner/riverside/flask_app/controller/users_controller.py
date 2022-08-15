from flask import render_template, request, redirect, session, Flask
from flask_app import app
from flask import flash
import smtplib
import ssl
from flask_app.models.user import User
from flask_mail import Mail, Message
import os
from datetime import datetime
mail = Mail(app)


@app.route('/')
def root():
    return redirect('/cleaning-service/home')


@app.route('/cleaning-service/home')
def home():

    return render_template('home.html', now=datetime.utcnow())


@app.template_filter('dateFormat')
def datetimeFormat(value, format='%Y'):
    return value.strftime(format)


@app.route("/cleaning-service/contact/submitted", methods=["POST"])
def contactForm():
    if not User.validate_form(request.form):
        print("Failed Validation")
        return redirect("/cleaning-service/home#Contact-Us")
    else:
        print("Grabbing Form Details")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        print("grabbed form inputs")

        msg = Message(
            f"New Website E-mail from: {name}",
            sender="support@myriversidecleaner.com",
            recipients=["support@myriversidecleaner.com"]
        )

        msg.body = (
            f"\n\nClients Name: {name}\n\nEmail: {email}\n\nPhone Number:{phone}\n\nMessage: {message}")
        print("done with formatting email")
        print(msg)
        mail.send(msg)

        flash("Message was Succesfully sent ", "success")
        print("Message was Succesfully sent ")

    print("done")

    return redirect("/cleaning-service/home#Contact-Us")
