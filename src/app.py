from flask import Flask
from src.routes import routes

class Application:

    app: Flask

    def __init__(self):
        self.app.secret_key = "asdasdasdad"
        self.app = Flask(__name__)
        self.__settings()
        self.__register_routes()

    def start(self):
        try:
            self.app.run(host="localhost", port=4000, debug=True, load_dotenv=True)
        except:
            pass

    """def __settings(self) -> None:
        try:
            self.app.config.from_mapping(
                SECRET_KEY="AJSLDHNASKJDBNALSDNA"
            )
        except Exception as e:
            pass"""
    
    def __register_routes(self) -> None:
        self.app.add_url_rule(routes['index'], view_func=routes['index_controller'], methods=['GET'])