#!/usr/bin/env pytuhon3
"""HNGx Stage 2 API module"""

import os
from flask import Flask, jsonify

from api.v2.views import app_views
from models.person import db, Person


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'hngx.db')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
db.init_app(app)


with app.app_context():
    db.create_all()


@app.errorhandler(400)
def not_found(error) -> str:
    """Handle 400 errors"""
    return jsonify({"error": error.description}), 400


@app.errorhandler(404)
def not_found(error) -> str:
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run()
