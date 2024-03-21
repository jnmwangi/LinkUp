from db import db
from sqlalchemy_serializer import SerializerMixin

class Service(db.Model, SerializerMixin):
    
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    media = db.Column(db.String)
    price = db.Column(db.Integer, default=0)
    
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    serialize_rules = ("-user.services",)