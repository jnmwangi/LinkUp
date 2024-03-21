from flask_restful import Resource
from flask import request, make_response, jsonify
from db import db

class View(Resource):
    
    def __init__(self, model) -> None:
        super().__init__()
        self.Model = model
        
    def get(self):
        records = self.Model.query.all()
        response =[record.to_dict() for record in records]
        
        return make_response(jsonify(response))
            

class ViewByIdView(Resource):
    
    
    def __init__(self, model) -> None:
        super().__init__()
        self.Model = model
        
    def get(self, id):
        
        record = self.Model.query.filter_by(id=id).first()
        
        if record == None:
            return make_response(jsonify({"error":"That record does not exists"}), 404)
        
        return make_response(jsonify(record.to_dict()), 200)
    
    def patch(self, id):
        record = self.Model.query.filter_by(id=id).first()
        
        if record == None:
            return make_response(jsonify({"error":"That record does not exists"}), 404)
        
        data = request.get_json()
        for attr in data:
            setattr(record, attr, data[attr])
            
        db.session.add(record)
        db.session.commit()
        
        return make_response(jsonify(record.to_dict()), 200)
    
    def delete(self, id):
        record = self.Model.query.filter_by(id=id).first()
        
        if record == None:
            return make_response(jsonify({"error":"That record does not exists"}), 404)
        
        db.session.delete(record)
        db.session.commit()
        
        return make_response(jsonify({"message":"Record deleted"}), 200)