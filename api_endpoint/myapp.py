#!/usr/bin/python3
from datetime import date, datetime
from flask import Flask, jsonify, make_response, request, abort
from flask_cors import CORS
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory (which contains 'project_directory') to the Python path
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

from models.user import User
from models import storage


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@app.route("/api", methods=["POST"], strict_slashes=False)
def create_user():
    """Creates a new user"""
    if not request.get_json() or "name" not in request.get_json():
        abort(400)

    data = request.get_json()
    user = User(**data)
    storage.save(user)
    return jsonify(user.to_dict())


@app.route("/api/<string:id>", methods=["GET"], strict_slashes=False)
def get_user(id):
    """Retrieves an user"""
    user = storage.get_details(id)
    if user == None:
        abort(404)
    return jsonify(user.to_dict())


@app.route("/api/<string:id>", methods=["DELETE"], strict_slashes=False)
def delete_user(id):
    """deletes a user"""
    user = storage.get_details(id)
    if user == None:
        abort(404)
    storage.delete(user)
    return jsonify({"Delete": "success"})


@app.route("/api/<string:id>", methods=["PUT"], strict_slashes=False)
def update_user(id):
    """Update a user"""
    if not request.get_json() or "name" not in request.get_json():
        abort(400)
    data = request.get_json()
    user = storage.get_details(id)
    if not user:
        abort(404)
    for k, v in data.items():
        if k == "name":
            user.name = v
    storage.save(user)
    return jsonify(user.to_dict())


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
