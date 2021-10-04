from flask import Flask
from src.routes import routes
from flask_cors import CORS

class Application:

    app: Flask

    def __init__(self):
        self.app = Flask(__name__)
        self.__register_routes()

    def start(self):
        try:
            self.app.run(host="localhost", port=4000, debug=True, load_dotenv=True)
        except:
            pass

    def __settings(self) -> None:
        try:
            self.app.config.from_mapping(
                SECRET_KEY="'59;R,#aME%^urS]ux0JP1GGMv2ii531;12y0uNK~G8A9h=tE._<wr&^#b2*@/fcF_aqqqRQW8z>L(A;OtWC@Y&nh!T3_TvH5T=^"
            )
            CORS(self.app, resources={
                r"/*": {
                    "origins": ["http://localhost:4200"]
                }
            }, support_credentials=True)
        except Exception as e:
            pass
    
    def __register_routes(self) -> None:
        self.app.add_url_rule(routes['index'], view_func=routes['index_controller'], methods=['GET'])
        self.app.add_url_rule(routes['signup'], view_func=routes['signup_controller'], methods=['POST', 'GET'])
        self.app.add_url_rule(routes['signin'], view_func=routes['signin_controller'], methods=['POST', 'GET'])
        self.app.add_url_rule(routes["admin_users"], view_func=routes["admin_users_controller"])
        self.app.add_url_rule(routes["admin_employees"], view_func=routes["admin_employees_controller"])
        self.app.add_url_rule(routes["favorites"], view_func=routes["favorites_controller"])
        self.app.add_url_rule(routes["appointments"], view_func=routes["appointments_controller"])
