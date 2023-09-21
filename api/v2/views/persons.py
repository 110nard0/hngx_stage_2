#!/usr/bin/env python3
"""Module of User views
"""
from flask import abort, jsonify, make_response, request
from markupsafe import escape
from mongoengine.errors import NotUniqueError, ValidationError
from typing import Union

from api.v2.views import app_views
from models.person import Person


@app_views.route('/', methods=['GET'], strict_slashes=False)
def view_persons() -> str:
    """ GET /api
    Return:
      - List of all Person objects JSON represented
    """
    persons = [person.to_dict() for person in Person.objects]
    return make_response(jsonify(persons), 200)


@app_views.route('/<user_id>', methods=['GET'], strict_slashes=False)
def view_person(user_id: Union[int, str]) -> str:
    """ GET /api/user_id
    Path parameter:
      - Person ID
    Return:
      - Person object JSON represented
      - 404 if Person ID does not exist
    """
    try:
        if Person.validate_id(user_id):
            person = Person.objects(id=user_id)[0]
        else:
            if Person.validate_name(user_id):
                person = Person.objects(name=user_id)[0]
            else:
                abort(404,
                      description="UID must be a valid string (name or id)")
    except (IndexError, ValidationError):
        abort(404,
              description="User not found")
    return make_response(jsonify(person.to_dict()), 200)



@app_views.route('/', methods=['POST'], strict_slashes=False)
def create_person() -> str:
    """ POST /api
    JSON body:
      - name
    Return:
      - Person object JSON represented
      - 400 if unable to create Person
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    name = request.get_json().get('name')
    if not Person.validate_name(name):
        abort(400, description="Name must be a string")

    person = Person(name=escape(name))
    try:
        person.validate()
        person.save()
    except (NotUniqueError, ValidationError):
        abort(400, description="Wrong input format or duplicate name supplied")
    return make_response(jsonify(person.to_dict()), 201)


@app_views.route('/<user_id>', methods=['PUT'], strict_slashes=False)
def update_person(user_id: Union[int, str]) -> str:
    """ PUT /api/user_id
    Path parameter:
      - Person ID
    JSON body:
      - name
    Return:
      - User object JSON represented
      - 400 if unable to update Person
      - 404 if Person ID does not exist
    """
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    name = request.get_json().get('name')
    if not Person.validate_name(name):
        abort(400, description="Name must be a string")

    try:
        if Person.validate_id(user_id):
            person = Person.objects(id=user_id)[0]
        else:
            if Person.validate_name(user_id):
                person = Person.objects(name=user_id)[0]
            else:
                abort(404,
                      description="UID must be a valid string (name or id)")
    except (IndexError, ValidationError):
        abort(404,
              description="User not found")

    person.name = escape(name)
    try:
        person.validate()
        person.save()
    except (NotUniqueError, ValidationError):
        abort(400, description="Wrong input format or duplicate name supplied")
    return make_response(jsonify(person.to_dict()), 200)


@app_views.route('/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_person(user_id: Union[int, str]):
    """ DELETE /api/user_id
    Path parameter:
      - Person ID
    Return:
      - Empty JSON if Person object has been correctly deleted
      - 400 if unable to delete Person
      - 404 if Person ID does not exist
    """
    try:
        if Person.validate_id(user_id):
            person = Person.objects(id=user_id)[0]
        else:
            if Person.validate_name(user_id):
                person = Person.objects(name=user_id)[0]
            else:
                abort(404,
                      description="UID must be a valid string (name or id)")
    except (IndexError, ValidationError):
        abort(404,
              description="User not found")
    person.delete()
    return make_response(jsonify({}), 204)
