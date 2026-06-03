from functools import wraps
from flask import request, jsonify


def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = request.user.get("role")

            if user_role not in roles:
                return jsonify({
                    "message": "Access Denied"
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator