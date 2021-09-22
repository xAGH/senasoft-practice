from src.controllers import IndexController

routes = {
    "index": "/", "index_controller": IndexController.as_view("index")
}