from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash 


db = "homescope"


class Homes:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.street_address = data ['street_address']
        # self.city = data ['city']
        # self.state = data ['state']
        # self.zipcode = data ['zipcode']
        self.description= data['description']
        # self.bed = data['bed']
        # self.bath = ['bath']
        # self.sq_ft = ['sq_ft']
        self.price = data['price']
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
            creator = user.Users(user_homes_data)
            my_homes.maker= creator
            home_list.append(my_homes)
        print(home_list)
        return home_list





    @classmethod
    def fetch_id(cls,data):
        query = "SELECT * FROM homes JOIN users ON homes.user_id = users.id WHERE homes.id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        if not results:
            return False
        results = results[0]
        print(results)
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
        my_homes.maker = user.Users(user_homes_data)
        return my_homes


    @classmethod
    def fetch_by_user_id(cls,data):
        query = "SELECT * FROM homes JOIN users ON homes.user_id = users.id WHERE homes.id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        print('working')
        print(results)
        if not results:
            return False
        print(results)
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
            my_homes.maker = user.Users(the_creator)
            colosseum.append(my_homes)
        return colosseum




    @classmethod
    def save(cls,data_form):
        query = "INSERT INTO homes (name, street_address, description, price ,user_id) VALUES (%(name)s, %(street_address)s, %(description)s, %(price)s,%(user_id)s);"
        return connectToMySQL(db).query_db(query,data_form)





    @classmethod
    def update(cls, data_form):
        query = "UPDATE homes SET name = %(name)s, street_address = %(street_address)s, description = %(description)s, price = %(price)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data_form)




    @classmethod
    def delete(cls,data):
        query = " DELETE FROM homes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)
        





    @staticmethod
    def validating_homes(data_form):
        is_valid = True
        if len(data_form['name']) < 3:
            flash("Name must be 3 characters minimum.")
            is_valid = False
        if len(data_form['street_address']) < 10:
            flash("Street address must be 10 characters minimum.")
            is_valid = False
        if len(data_form['description']) < 8:
            flash("Description must be at least 8 characters.")
            is_valid = False
        if len(data_form['price']) < 5:
            flash("Price must be at least 5 digit.")
            is_valid = False
        return is_valid


