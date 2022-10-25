from unicodedata import name
from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size

planets = [
    Planet(1, "Earth", "3rd planet from sun, inhabits life", "7,917.5 mi"),
    Planet(2, "Mars", "4th planet from the sun, cold dusty desert", "4,212.3 mi"),
    Planet(3, "Saturn", "2nd largest planet, Adorned with thousands of beautiful ringlets", "72,367 mi")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("",methods=["GET"])
def handle_planets_data():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        }), 200
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} invalid"}, 400))
        
    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message":f"planet {planet_id} not found"}, 404))

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return jsonify({
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "size": planet.size
    }), 200