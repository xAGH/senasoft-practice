from flask import request, make_response, jsonify 
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import Model
import jwt, datetime

class IndexController(MethodView):

    def get(self):
        return "Hello World!"

class SigninController(MethodView):

    decorators = []

    def get(self):
        pass

    def post(self):
        pass

class SignupController(MethodView):

    decorators = []

    def __init__(self) -> None:
        self.model = Model()

    def get(self):
        return "Signup a user"
    
    def post(self):
        if request.is_json:
            email = request.json['email']
            name = request.json['name']
            password = request.json['password']
            verify_email = self.model.fetch_one("SELECT * FROM customers WHERE email = %s", (email, ))
            if(not verify_email or verify_email is None):
                hash_password = generate_password_hash(password)
                self.model.execute_query("INSERT INTO customers(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
                token: str = jwt.encode({
                    "name": name,
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                }, "secretkey")
                response = make_response(jsonify({
                    "message": "Congrats! Your user was create",
                    "token": token
                }), 201)
                response.headers['Authorization'] = token
                return response
            response = make_response(jsonify({
                "message": "User already exists on the database"
            }), 401)
            return response
        response = make_response(jsonify({
            "message": "Please send me a JSON FORMAT"
        }), 400)
        return response
