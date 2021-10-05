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
                token = request.headers.get('Authorization')
                uid_token = str(jwt.decode(token, "secretkey", algorithms=['HS256'])["subject"])
                if process == True:
                    self.model.execute_query("UPDATE users SET is_admin = '1' WHERE uid = %s", (uid))
                    response = make_response(jsonify({
                        "message":"The user now has admin permissions."
                    }), 200)

                elif process == False:
                    if uid == uid_token:
                        response = make_response(jsonify({
                            "message":"You cannot remove your admin permissions."
                        }), 400)
                    else:
                        self.model.execute_query("UPDATE users SET is_admin = '0' WHERE uid = %s", (uid))
                        response = make_response(jsonify({
                            "message":"The user now hasn't admin permissions."
                        }), 200)

                else:
                    response = make_response(jsonify({
                        "message":"Please send me a valid process. False -> Delete admin permission or True -> Add admin permission."
                    }), 406)
            
            except:
                response = make_response(jsonify({
                        "message":"Please send me a 'process' and an 'uid' key"
                    }), 406)

        return response

    def delete(self):
        response = make_response(jsonify({
                "message": "Please send me a JSON FORMAT"
            }), 400)

        if request.is_json:
            try:
                uid = request.json['uid']
                token = request.headers['Authorization']
                uid_token = str(jwt.decode(token, "secretkey", algorithms=['HS256'])["subject"])
                if uid_token == uid:
                    response = make_response(jsonify({
                        "message": "You can't delete yourself."
                    }), 400)

                else:
                    self.model.execute_query("DELETE FROM users WHERE uid = %s", uid)
                    response = make_response(jsonify({
                        "message": "The user was successfully deleted"
                    }), 200)

            except:
                response = make_response(jsonify({
                    "message":"Please send me an 'uid' key"
                }), 406)

        return response


class AdminEmployeesController(MethodView):

    decorators = [verify_token, verify_role]

    def __init__(self) -> None:
        self.model = Model()

    def get(self):
        data = self.model.fetch_all("SELECT * FROM employees")
        return make_response(jsonify({
            "employees_data" : data
        }), 200)

    def post(self):
        response = make_response(jsonify({
            "message" : "Please send me a JSON FORMAT"
        }), 400)

        if request.is_json:
            try:
                response = make_response(jsonify({
                    "message" : "That service does'nt exists."
                }), 400)
                name = request.json['name']
                lastname = request.json['lastname']
                service = request.json['service']
                services = self.model.fetch_one("SELECT uid FROM services where uid = %s", service)
                if services != None:
                    self.model.execute_query("INSERT INTO employees(name, lastname, service) values(%s, %s, %s)", (name, lastname, service))
                    uid = self.model.fetch_one("SELECT uid FROM employees ORDER BY uid DESC LIMIT 1")[0]
                    print(uid)
                    self.model.execute_query(f"""INSERT INTO employee_schedule values
                    ({uid},'D', '1'),
                    ({uid},'T', '1'),
                    ({uid},'N', '1')""")
                    response = make_response(jsonify({
                        "message": "The employee was created successfully."
                    }), 201)
            except Exception as e:
                response = make_response(jsonify({
                    "message":"Please send me a name, a lastname and a service key"
                }), 406)

        return response

    def delete(self):
        response = make_response(jsonify({
            "message" : "Please send me a JSON FORMAT"
        }), 400)
        if request.is_json:

            try:
                uid = request.json['uid']
                self.model.execute_query("DELETE FROM employees WHERE uid = %s", uid)
                response = make_response(jsonify({
                    "message": "The user was successfully deleted"
                }), 200)

            except:
                response = make_response(jsonify({
                    "message":"Please send me an 'uid' key"
                }), 406)
            
        return response

class FavoritesController(MethodView):

    decorators = [verify_token]

    def __init__(self) -> None:
        self.model = Model()
        self.token = request.headers['Authorization']

    def get(self):
        response = make_response(jsonify({
            "message" : "Please send me a JSON FORMAT"
        }), 400)
        if request.is_json:
            
                schedule = request.json['schedule']
                user_uid = str(jwt.decode(self.token, "secretkey", algorithms=['HS256'])["subject"])
                favorites = self.model.fetch_all(f"""SELECT e.uid, e.name, e.lastname, e.service 
                FROM favorites f, employees e, employee_schedule es WHERE f.employee = e.uid and 
                es.employee = e.uid AND es.schedule = '{schedule}' and es.status = '1'""")
                if favorites:
                    print(user_uid)
                    employees_available = self.model.fetch_all(f"""SELECT e.uid, e.name, e.lastname, e.service 
                    FROM favorites f, employees e, employee_schedule es WHERE f.employee != e.uid and f.user = {user_uid}
                    and es.employee = e.uid AND es.schedule = '{schedule}' and es.status = '1';""")

                    employees_unavailable = self.model.fetch_all(f"""SELECT e.uid, e.name, e.lastname, e.service 
                    FROM favorites f, employees e, employee_schedule es WHERE f.employee != e.uid and f.user = {user_uid}
                    and es.employee = e.uid AND es.schedule = '{schedule}' and es.status = '0';""")
                else:
                    favorites = False
                    employees_available = self.model.fetch_all(f"""SELECT e.uid, e.name, e.lastname, e.service FROM 
                    employees e, employee_schedule es WHERE e.uid = es.employee AND es.schedule = '{schedule}' and es.status = '1';""")
                    employees_unavailable = self.model.fetch_all(f"""SELECT e.uid, e.name, e.lastname, e.service FROM 
                    employees e, employee_schedule es WHERE e.uid = es.employee AND es.schedule = '{schedule}' and es.status = '0';""")
                
                if len(employees_unavailable) < 1:
                    employees_unavailable = False

                response = make_response(jsonify({
                    "favorites_employees" : favorites,
                    "available_employees": employees_available,
                    "unavailable_employees": employees_unavailable
                }), 200)
            
        return response

    def post(self):
        response = make_response(jsonify({
            "message" : "Please send me a JSON FORMAT"
        }), 400)
        if request.is_json:

            try:
                user_uid = int(jwt.decode(self.token, "secretkey", algorithms=['HS256'])["subject"])
                employee_uid = int(request.json['employee_uid'])
                exists = self.model.fetch_one("SELECT * FROM favorites WHERE user = %s AND employee = %s", (user_uid, employee_uid))
                response = make_response(jsonify({
                        "message":"The employee is actually a user's favorite."
                    }), 200)
                if not exists:
                    self.model.execute_query("INSERT INTO favorites VALUES(%s, %s)", (employee_uid, user_uid))
                    response = make_response(jsonify({
                        "message":"The employee was added to the user's favorites successfully."
                    }), 201)

            except Exception as e:
                response = make_response(jsonify({
                    "message":"Please send me an 'employee_uid' key (int)",
                    "a":f"{e}"
                }), 406)
            
        return response

    def delete(self):
        response = make_response(jsonify({
            "message" : "Please send me a JSON FORMAT"
        }), 400)
        if request.is_json:

            try:
                user_uid = int(jwt.decode(self.token, "secretkey", algorithms=['HS256'])["subject"])
                employee_uid = request.json['employee_uid']
                self.model.execute_query(f"DELETE FROM favorites WHERE user = {user_uid} AND employee = {employee_uid}")
                response = make_response(jsonify({
                    "message": "The user was successfully deleted"
                }), 200)

            except:
                response = make_response(jsonify({
                    "message":"Please send me an 'employee_uid' key"
                }), 406)
            
        return response

class AppointmentsController(MethodView):

    decorators = [verify_token]

    def __init__(self) -> None:
        self.model = Model()

    @verify_role
    def get(self):
        data = self.model.fetch_all("SELECT * FROM appointments")
        return make_response(jsonify({
            "appointments": data
        }), 200)
    
    def post(self):
        response = make_response(jsonify({
            "message" : "Please send me a JSON FORMAT"
        }), 400)

        if request.is_json:
            try:
                pass
            except:
                response = make_response(jsonify({
                    "message":"Please send me an 'employee_uid' and a 'schedule' key"
                }), 406)