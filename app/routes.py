from flask import request 
from flask import Blueprint
from flask import jsonify
from app import db
from app.model.planet import Planet 


planet_bp = Blueprint("planets", __name__, url_prefix="/planets")



@planet_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name = request_body['name'], description = request_body['description'], 
                    distance_from_sun = request_body['distance_from_sun'])
    db.session.add(new_planet)
    db.session.commit()

    return {"Success": True, 
            "Message": f"Planet with {new_planet.id} has been created"}, 201


