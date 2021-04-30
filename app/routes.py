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


@planet_bp.route("", methods=["GET"])
def display_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response, 200)

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_single_planets(planet_id):
    
    planet = Planet.query.get(planet_id)

    if planet:
        return planet.to_json(), 200

    return {
        "message": f"Planet with {planet_id} was not found",
        "success": False
    }, 404
