from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_api import status

post_api = Blueprint("post", __name__)

@post_api.route("", methods=["POST"])
@jwt_required()
def post_create():
    return jsonify(success=True), status.HTTP_200_OK
