from flask import (
   Blueprint,
   jsonify,
   request
)
import requests
from config import (
   PRODUCT_SERVICE_URL
)
from middleware.jwt_middleware import (
   token_required
)
product_bp = Blueprint(
   "product_bp",
   __name__
)
# GET Products
@product_bp.route(
   "/products",
   methods=["GET"]
)
@token_required
def get_products():
   response = requests.get(
       f"{PRODUCT_SERVICE_URL}/products"
   )
   return jsonify(
       response.json()
   )

# CREATE Product
@product_bp.route(
   "/products",
   methods=["POST"]
)
@token_required
def create_product():
   response = requests.post(
       f"{PRODUCT_SERVICE_URL}/products",
       json=request.json
   )
   return jsonify(
       response.json()
   ), response.status_code

# GET Product
@product_bp.route(
   "/products/<int:id>",
   methods=["GET"]
)
@token_required
def get_product(id):
   response = requests.get(
       f"{PRODUCT_SERVICE_URL}/products/{id}"
   )
   return jsonify(
       response.json()
   )

# UPDATE Product
@product_bp.route(
   "/products/<int:id>",
   methods=["PUT"]
)
@token_required
def update_product(id):
   response = requests.put(
       f"{PRODUCT_SERVICE_URL}/products/{id}",
       json=request.json
   )
   return jsonify(
       response.json()
   )

# DELETE Product
@product_bp.route(
   "/products/<int:id>",
   methods=["DELETE"]
)
@token_required
def delete_product(id):
   response = requests.delete(
       f"{PRODUCT_SERVICE_URL}/products/{id}"
   )
   return jsonify(
       response.json()
   )