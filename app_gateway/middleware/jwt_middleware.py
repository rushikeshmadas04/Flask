import jwt
from functools import wraps
from flask import request, jsonify
from config import SECRET_KEY

def token_required(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       auth_header = request.headers.get("Authorization")
       if not auth_header:
           return jsonify({
               "message": "Token Missing"
           }), 401
       try:
           token = auth_header.split()[1]
           decoded = jwt.decode(
               token,
               SECRET_KEY,
               algorithms=["HS256"]
           )
           request.user = decoded
       except Exception:
           return jsonify({
               "message": "Invalid Token"
           }), 401
       return func(*args, **kwargs)
   return wrapper