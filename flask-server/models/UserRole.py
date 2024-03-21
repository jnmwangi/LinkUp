from db import db
from sqlalchemy_serializer import SerializerMixin

class UserRole(db.Model, SerializerMixin):
    __tablename__ = "user_roles"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    
    user = db.relationship("User", back_populates="roles")
    role = db.relationship("Role", back_populates="users")
    serialize_rules = ("-user.roles", "-role.users")