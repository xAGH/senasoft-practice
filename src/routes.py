from src.controllers import IndexController, SignupController, SigninController, AdminUsersController, AdminEmployeesController, FavoritesController, AppointmentsController

routes = {
    "index": "/", "index_controller": IndexController.as_view("index"),
    "signup": "/signup", "signup_controller": SignupController.as_view("signup"),
    "signin": "/signin", "signin_controller": SigninController.as_view("signin"),
    "admin_users": "/admin/users", "admin_users_controller": AdminUsersController.as_view("admin_users"),
    "admin_employees": "/admin/employees", "admin_employees_controller": AdminEmployeesController.as_view("admin_employees"),
    "favorites":"/favorites", "favorites_controller":FavoritesController.as_view("favorites"),
    "appointments":"/appointments", "appointments_controller":AppointmentsController.as_view("appointments")
}
