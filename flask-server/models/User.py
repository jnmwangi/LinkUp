from db import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sp_app import bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    fullname = db.Column(db.String(50), nullable=False)
    _password_hash = db.Column(db.String(255), unique=True)    
    
    services = db.relationship("Service", backref="user")
    roles = db.relationship("UserRole", back_populates="user")
    
    serialize_rules = (
        "id", "username", "email", 
        "fullname", 
        "-services.user", "-_password_hash", 
        "-roles.user")
    
    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Invalid email")
        
        return email
    
    @hybrid_property
    def password(self):
        return self._password_hash
    
    @password.setter
    def password(self, raw_password):
        password_hash = bcrypt.generate_password_hash(raw_password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
        
    def authenticate(self, raw_password):
        return bcrypt.check_password_hash(
            self._password_hash, raw_password.encode('utf-8')
        )