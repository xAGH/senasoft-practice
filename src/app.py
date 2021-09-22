from flask import Flask
from src.routes import routes

class Application:

    app: Flask

    def __init__(self):
        self.app.secret_key = "'59;R,#aME%^urS]ux0JP1GGMv2ii531;12y0uNK~G8A9h=tE._<wr&^#b2*@/fcF_aqqqRQW8z>L(A;OtWC@Y&nh!T3_TvH5T=^"
        self.app = Flask(__name__)
        self.__register_routes()

    def start(self):
        try:
            self.app.run(host="localhost", port=4000, debug=True, load_dotenv=True)
        except:
            pass

    def __register_routes(self) -> None:
        self.app.add_url_rule(routes['index'], view_func=routes['index_controller'], methods=['GET'])