from flask_restful import Resource
from flask import make_response, request, jsonify
from models import User
from db import db

# C CREATE -> POST
# R READ   -> GET 
# U UPDATE -> PATCH / PUT
# D DELETE -> DELETE

class UsersView(Resource):
    
    def get(self):
        users = User.query.all()
        response =[user.to_dict() for user in users]
        
        return make_response(jsonify(response))
    
    def post(self):
        
        # try:
        data = request.get_json()
        user = User(
            fullname=data["fullname"],
            email=data["email"],
            username=data["username"],
            password=data["password"]
        )
        
        db.session.add(user)
        db.session.commit()
        
        return make_response(jsonify(user.to_dict()), 201)
        
        # except ValueError:
        #     return make_response(jsonify({"error":"Invalid data"}), 400)
        # except:
        #     return make_response(jsonify({"error":"Error occur"}), 400)
        

class UserByIdView(Resource):
    
    def get(self, id):
        
        user = User.query.filter_by(id=id).first()
        
        if user == None:
            return make_response(jsonify({"error":"User does not exists"}), 404)
        
        return make_response(jsonify(user.to_dict()), 200)
    
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        
        if user == None:
            return make_response(jsonify({"error":"User does not exists"}), 404)
        
        data = request.get_json()
        for attr in data:
            setattr(user, attr, data[attr])
            
        db.session.add(user)
        db.session.commit()
        
        return make_response(jsonify(user.to_dict()), 200)
    
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        
        if user == None:
            return make_response(jsonify({"error":"User does not exists"}), 404)
        
        db.session.delete(user)
        db.session.commit()
        
        return make_response(jsonify({"message":"User deleted"}), 200)