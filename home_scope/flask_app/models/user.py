from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re


db = "homescope"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']




    @classmethod
    def save(cls,data_form):
        data_hashing = {
            'first_name': data_form['first_name'],
            'last_name': data_form['last_name'],
            'email': data_form['email'],
            'password': bcrypt.generate_password_hash(data_form['password']),
        }
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(db).query_db(query,data_hashing)


    @classmethod
    def fetch_email(cls,data):
        query = " SELECT * FROM users WHERE email = %(email)s; "
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        return cls(result[0])



    @classmethod
    def fetch_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False
        return cls(result[0])


    @staticmethod
    def validate_regis_form(data_form):
        valid = True
        if len(data_form['email']) < 1:
            flash("Email can't be empty.","register")
            valid = False
        elif not EMAIL_REGEX.match(data_form['email']):
            flash("Email address invalid.","register")
            valid = False
        elif User.fetch_email(data_form):
            flash("User exists for email.","register")
            valid = False
        if len(data_form['password']) < 6:
            flash("Password needs 6 characters minimum.","register")
            valid = False
        if data_form['password'] != data_form['confirm_password']:
            flash("Passwords must match.","register")
            valid = False
        if len(data_form['first_name']) < 3:
            flash("First name must be 3 characters minimum.","register")
            valid = False
        if len(data_form['last_name']) < 3:
            flash("Last name must be 3 characters minimum.","register")
            valid = False
        return valid



    @staticmethod
    def login_validator(data_form):
        if not EMAIL_REGEX.match(data_form['email']):
            flash("Email/Password invalid.","login")
            return False
        the_user = User.fetch_email(data_form)
        if not the_user:
            flash("Email/Password invalid.","login")
            return False
        if not bcrypt.check_password_hash(the_user.password, data_form['password']):
            flash("Email/Password invalid.","login")
            return False
        return the_user

