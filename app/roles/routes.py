from flask import Blueprint, jsonify

from app.roles.services import list_roles

roles_bp = Blueprint("roles", __name__, url_prefix="/roles")


@roles_bp.get("/")
def roles_index():
    return jsonify({"roles": list_roles()})
