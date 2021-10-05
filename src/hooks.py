from flask import request, jsonify, make_response
from functools import wraps
import jwt

def verify_token(function):
    """
        @function decoradora.
        @verify_token toma la cabecera enviada por el cliente y verifica que la firma del token sea la misma.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        try:
            read_data = jwt.decode(token, "secretkey", algorithms=['HS256'])
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


def verify_role(function):
    """
    @function decoradora.
    @verify_role toma la cabecera enviada por el cliente y verifica que el usuario tenga permisos de amdmin.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        
        token = request.headers.get('Authorization')

        try:
            read_data = jwt.decode(token, "secretkey", algorithms=['HS256'])
            if read_data['is_admin'] == '0':
                response = make_response(jsonify({
                    "message": "No permissions"
                }), 401)
                return response
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
       
        return function(*args, **kwargs)
    return wrapper