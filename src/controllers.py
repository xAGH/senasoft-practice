from flask import request, make_response, jsonify 
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from src.models import Model
from src.hooks import verify_role, verify_token
import jwt, datetime

class IndexController(MethodView):

    decorators = [verify_token]

    def get(self):
        return "Hello World!"

class SigninController(MethodView):

    decorators = []

    def __init__(self) -> None:
        self.model = Model()

    def get(self):
        pass

    def post(self):
        if request.is_json:
            email = request.json['email']
            password = request.json['password']
            verify_data = self.model.fetch_one("SELECT * FROM users WHERE email = %s", (email, ))
            if(verify_data or verify_data is not None):
                verify_password = check_password_hash(verify_data[3], password)
                if(verify_password):
                    token: str = jwt.encode({
                        "subject": verify_data[0],
                        "email": verify_data[2],
                        "is_admin": verify_data[4],
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                    }, "secretkey")
                    response = make_response(jsonify({
                        "message": f"Success! You're logged in {verify_data[1]}",
                        "token": token
                    }), 201)
                    response.headers['Authorization'] = token
                    return response
            return make_response(jsonify({
                "message": "Wrong credentials"
            }), 401)
        return make_response(jsonify({
            "message": "please send a JSON format"
        }), 401)

class SignupController(MethodView):

    decorators = []

    def __init__(self) -> None:
        self.model = Model()

    def post(self):
        if request.is_json:
            email = request.json['email']
            name = request.json['name']
            password = request.json['password']
            verify_email = self.model.fetch_one("SELECT * FROM users WHERE email = %s", (email))
            if(not verify_email or verify_email is None):
                hash_password = generate_password_hash(password)
                self.model.execute_query("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (name, email, hash_password))
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

class AdminUsersController(MethodView):

    decorators = [verify_token, verify_role]

    def __init__(self) -> None:
        self.model = Model()

    def get(self):
        data = self.model.fetch_all("SELECT * FROM users")
        return make_response(jsonify({
            "users_data" : data
        }), 200)

    def patch(self):
        response = make_response(jsonify({
                "message": "Please send me a JSON FORMAT"
            }), 400)
        if request.is_json:
            try:
                uid = request.json['uid']
                process = request.json['process']
                if process == True:
                    self.model.execute_query("UPDATE users SET is_admin = '1' WHERE uid = %s", (uid))
                    response = make_response(jsonify({
                        "Success":"The user now has admin permissions."
                    }), 200)

                elif process == False:
                    self.model.execute_query("UPDATE users SET is_admin = '0' WHERE uid = %s", (uid))
                    response = make_response(jsonify({
                        "Success":"The user now hasn't admin permissions."
                    }), 200)

                else:
                    response = make_response(jsonify({
                        "message":"Please send me a valid process. False -> Delete admin permission or True -> Add admin permission."
                    }), 200)

                return response
            
            except:
                response = make_response(jsonify({
                        "message":"Please send me a 'process' and a 'uid' key"
                    }), 200)

        return response


class AdminEmployeesController(MethodView):

    decorators = [verify_token, verify_role]

    def __init__(self) -> None:
        self.model = Model()

    def get(self):
        data = self.model.fetch_all("SELECT * FROM employees")
        return make_response(jsonify({
            "employees_data" : data
        }), 201)