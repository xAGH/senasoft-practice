from flask import request, jsonify, make_response
from functools import wraps
import jwt

"""
    @function decoradora.
    @verify_token toma la cabecera enviada por el cliente y verifica que la firma del token sea la misma.
"""
def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        try:
            read_data = jwt.decode(token, "secretkey", algorithms=['HS256'])
            print(read_data)
        except jwt.InvalidTokenError as e:
            response = make_response(jsonify({
                "message": "Token is missing or invalid"
            }), 401)
            return response
        except jwt.ExpiredSignatureError as e:
            response = make_response(jsonify({
                "message": "Token is expired"
            }), 401)
            return response
        except Exception as e:
            response = make_response(jsonify({
                "message": f"Token error: {e}"
            }), 401)
        return function(*args, **kwargs)
    return wrapper