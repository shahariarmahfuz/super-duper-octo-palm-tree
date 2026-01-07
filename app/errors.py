from flask import Flask, jsonify


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "not_found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "internal_server_error"}), 500
