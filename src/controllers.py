from flask import *
from flask.views import MethodView

class IndexController(MethodView):

    def get(self):
        return flash("Holasdlasda", "success")