from flask import flash
import re
from flask_app import app
import smtplib
import os


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.phone = data['phone']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_form(data):
        is_valid = True

        if not EMAIL_REGEX.match(data['email']):
            flash(" *Invalid email address", 'email')
            is_valid = False
        if len(data['name']) < 1:
            flash(" *Please Enter Your Name", 'name')
            is_valid = False
        if len(data['phone']) < 10:
            flash(" *Please Enter a Phone Number", 'phone')
            is_valid = False
        if len(data['message']) < 3:
            flash(" *Please Enter a message", 'message')
            is_valid = False

        return is_valid
