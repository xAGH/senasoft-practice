from src.controllers import IndexController, SignupController, SigninController, AdminUsersController, AdminEmployeesController

routes = {
    "index": "/", "index_controller": IndexController.as_view("index"),
    "signup": "/signup", "signup_controller": SignupController.as_view("signup"),
    "signin": "/signin", "signin_controller": SigninController.as_view("signin"),
    "admin_users": "/admin/users", "admin_users_controller": AdminUsersController.as_view("admin_users"),
    "admin_employees": "/admin/employees", "admin_employees_controller": AdminEmployeesController.as_view("admin_employees")
}
