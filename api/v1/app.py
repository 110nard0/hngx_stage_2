#!/usr/bin/env pytuhon3
"""HNGx Stage 1 API module"""

from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error) -> str:
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run()
