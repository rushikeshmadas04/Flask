from flask import (

    Blueprint,

    request,

    jsonify

)

import jwt

import datetime

from config import SECRET_KEY

auth_bp = Blueprint(

    "auth_bp",

    __name__

)

# Dummy Users

# For learning.

users = {
    'admin': {
        'password': 'admin123',
        'role': 'ADMIN'
    },
    'user': {
        'password': 'user123',
        'role': 'USER'
    }
}

# Login Route

@auth_bp.route(

    "/login",

    methods=[
        'POST'
    ]

)

def login():

    data = request.get_json()

    username = data["username"]

    password = data["password"]

    user = users.get(username)

    if not user:

        return jsonify({
            'message': 'Invalid User'
        }), 401

    if user["password"] != password:

        return jsonify({
            'message': 'Invalid Password'
        }), 401

    token = jwt.encode(

        {

            "username": username,

            "role": user["role"],

            "exp": (

                datetime.datetime.utcnow()

                + datetime.timedelta(hours=1)

            )

        },

        SECRET_KEY,

        algorithm="HS256"

    )

    return jsonify({

        "token": token

    })
 