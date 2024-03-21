from models import *
from flask_restful import Api
from views import *
from sp_app import app

api = Api(app)
api.add_resource(UsersView, "/users")
api.add_resource(UserByIdView, "/users/<int:id>")
api.add_resource(View, "/services", resource_class_kwargs={"model": Service})
api.add_resource(RoleView, "/roles", resource_class_kwargs={"model": Role})
api.add_resource(RoleById, "/roles", resource_class_kwargs={"model": Role})

if __name__ == "__main__":
    app.run(debug=True)