from flask import flash
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    @staticmethod
    def validate_user( user ):
        is_valid = True
        # prueba si un campo coincide con el patrón
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

@staticmethod
def validate_user(user):
    is_valid = True # asumimos que esto es true
    if len(user['first_name']) < 3:
        flash("Name must be at least 3 characters.")
        is_valid = False
    if len(user['last_name']) < 3:
        flash("Last name must be at least 3 characters.")
        is_valid = False
    if int(user['email']) < 3:
        flash("email must be at least charactes.")
        is_valid = False
    if len(user['password']) < 8:
        flash("password must be at least 8 characters.")
        is_valid = False
    return is_valid

class User:
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)

class User:
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])
