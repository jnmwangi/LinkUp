from db import db
from sqlalchemy_serializer import SerializerMixin

class Role(db.Model, SerializerMixin):
    
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    
    users = db.relationship("UserRole", back_populates="role")    
    serialize_rules = ("-users.role",)