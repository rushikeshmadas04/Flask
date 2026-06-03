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

# Dummy user store for demonstration purposes.
# In real applications, use a database.
users = {
    "admin": {
        "password": "admin123",
        "role": "ADMIN"
    },
    "user": {
        "password": "user123",
        "role": "USER"
    }
}


# LOGIN ROUTE
@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    username = data["username"]
    password = data["password"]

    user = users.get(username)

    if not user:
        return jsonify({
            "message": "Invalid User"
        }), 401

    if user["password"] != password:
        return jsonify({
            "message": "Invalid Password"
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
        "username": username,
        "role": user["role"],
        "token": token
    }), 200