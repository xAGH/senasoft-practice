from src.controllers import IndexController, SignupController

routes = {
    "index": "/", "index_controller": IndexController.as_view("index"),
    "signup": "/signup", "signup_controller": SignupController.as_view("signup"),
    "signin": "/signin", "signin_controller": SignupController.as_view("signin")
}