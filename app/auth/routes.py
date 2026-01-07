from flask import Blueprint, jsonify

from app.auth.services import authenticate_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.post("/login")
def login():
    user = authenticate_user()
    return jsonify({"user": user})
