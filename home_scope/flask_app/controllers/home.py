from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash 
import re

db = "homescope"

ZIP_REGEX = re.compile(r'\d{5}')
STATE_REGEX = re.compile(r'[a-zA-Z]{2}')
class Home:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.street_address = data ['street_address']
        self.city = data ['city']
        self.state = data ['state']
        self.zipcode = data ['zipcode']
        self.description= data['description']
        self.bed = data['bed']
        self.bath = ['bath']
        self.sq_ft = ['sq_ft']
        self.price = data['price']
        self.type = data['type']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = data['user_id']
        self.maker = None

    @classmethod
    def fetch_all(cls):
        query = "SELECT * FROM homes JOIN users ON homes.user_id = users.id;"
        results = connectToMySQL(db).query_db(query)
        home_list = []
        for rows in results:
            my_homes = cls(rows)
            user_homes_data = {
                "id":rows['users.id'],
                "first_name":rows['first_name'],
                "last_name": rows['last_name'],
                "email": rows['email'],
                "password": "",
                "created_at": rows['users.created_at'],
                "updated_at": rows['users.updated_at']
            }
            creator = user.User(user_homes_data)
            my_homes.maker= creator
            home_list.append(my_homes)
        return home_list





    @classmethod
    def fetch_id(cls,data):
        query = "SELECT * FROM homes JOIN users ON homes.user_id = users.id WHERE homes.id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        if not results:
            return False
        results = results[0]
        my_homes = cls(results)
        user_homes_data = {
            "id": results['users.id'],
            "first_name": results['first_name'],
            "last_name": results['last_name'],
            "email": results['email'],
            "password": "",
            "created_at": results['users.created_at'],
            "updated_at": results['users.updated_at']
        }
        my_homes.maker = user.User(user_homes_data)
        return my_homes


    @classmethod
    def fetch_by_user_id(cls, data):
        query = "SELECT * FROM homes JOIN users ON homes.user_id = users.id WHERE homes.id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        if not results:
            return False
        colosseum=[]
        for x in results:
            my_homes = cls(x)
            the_creator = {
                "id": results[0]['users.id'],
                "first_name": results[0]['first_name'],
                "last_name": results[0]['last_name'],
                "email": results[0]['email'],
                "password": "",
                "created_at": results[0]['users.created_at'],
                "updated_at": results[0]['users.updated_at']
            }
            my_homes.maker = user.User(the_creator)
            colosseum.append(my_homes)
        return colosseum




    @classmethod
    def save(cls,data_form):
        query = "INSERT INTO homes (name, street_address, city, state, zipcode, description, \
            bed, bath, sq_ft, price, image, user_id) VALUES (%(name)s, %(street_address)s, %(city)s, %(state)s, %(zipcode)s, \
            %(description)s, %(bed)s, %(bath)s, %(sq_ft)s, %(price)s, %(image)s, %(user_id)s);"
        results = connectToMySQL(db).query_db(query,data_form)
        print(results)
        return results



    @classmethod
    def update(cls, data_form):
        query = "UPDATE homes SET name = %(name)s, street_address = %(street_address)s, city = %(city)s, state = %(state)s, zipcode = %(zipcode)s, description = %(description)s, \
                bed = %(bed)s, bath = %(bath)s, sq_ft = %(sq_ft)s, price = %(price)s, image = %(image)s WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data_form)
        return results


    @classmethod
    def delete(cls,data):
        query = " DELETE FROM homes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
        

    @staticmethod
    def home_types():
        home_types = ['Single Family Homes', 'Multi Family Homes', 'Townhouse']
        return home_types



    @staticmethod
    def validating_homes(data_form):
        is_valid = True
        if len(data_form['name']) < 3:
            flash(u"Name must be 3 characters minimum.", "home_info")
            is_valid = False
        if len(data_form['street_address']) < 10:
            flash(u"Street address must be 10 characters minimum.", "home_info")
            is_valid = False
        if len(data_form['description']) < 8:
            flash(u"Description must be at least 8 characters.", "home_info")
            is_valid = False
        if not(data_form['price']) or int(data_form['price']) <= 0:
            flash(u"Invalid price.", "home_info")
            is_valid = False
        if not ZIP_REGEX.match(data_form['zipcode']):
            flash(u'Invalid zip code!', 'home_info')
        if not ZIP_REGEX.match(data_form['state']):
            flash(u'Invalid state!', 'home_info')
        if len(data_form['city'])  < 3:
            flash(u"Invalid city name", "home_info")
        if not(data_form['bed']) or int(data_form['bed']) <= 0:
            flash(u"Invalid bed counts.", "home_info")
        if not(data_form['sq_ft']) or int(data_form['sq_ft']) <= 0:
            flash(u"Invalid square feets.", "home_info")
        if not(data_form['bath']) or int(data_form['bath']) <= 0:
            flash(u"Invalid bath counts.", "home_info")
        return is_valid


