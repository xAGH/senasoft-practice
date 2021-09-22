from flask import *
from flask.views import MethodView

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

    def get(self):
        return "Signup a user"
    
    def post(self):
        if request.is_json:
            pass
        response = make_response(jsonify({
            "message": "Please send me a JSON FORMAT"
        }), 400)
        return response