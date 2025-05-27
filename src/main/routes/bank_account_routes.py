from flask import Blueprint, jsonify

bank_route_bp = Blueprint('bank_route', __name__)

@bank_route_bp.route("/", methods=["GET"])
def hello():
    return jsonify({"Hello": "World!"})

    