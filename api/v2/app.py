#!/usr/bin/env pytuhon3
"""HNGx Stage 2 API module"""
from flask import Flask, jsonify
from mongoengine import connect
from os import getenv

from api.v2.views import app_views
from models.person import Person


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

DB_URI = getenv('MONGODB_URI')


if DB_URI:
    connect(host=DB_URI)
else:
    connect(host="mongodb://127.0.0.1:27017/hngx")


@app.errorhandler(400)
def not_found(error) -> str:
    """Handle 400 errors"""
    return jsonify({"error": error.description}), 400


@app.errorhandler(404)
def not_found(error) -> str:
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    HOST = getenv('HOST_NAME', '0.0.0.0')
    PORT = getenv('PORT', 5000)
    app.run(HOST, PORT)
