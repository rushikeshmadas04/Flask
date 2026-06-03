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

from middleware.authorization import (
    role_required
)

product_bp = Blueprint(
    "product_bp",
    __name__
)


# GET ALL PRODUCTS
@product_bp.route(
    "/products",
    methods=["GET"]
)
@token_required
@role_required("ADMIN", "USER")
def get_products():
    response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products"
    )

    return jsonify(
        response.json()
    ), response.status_code


# CREATE PRODUCT
@product_bp.route(
    "/products",
    methods=["POST"]
)
@token_required
@role_required("ADMIN")
def create_product():
    response = requests.post(
        f"{PRODUCT_SERVICE_URL}/products",
        json=request.json
    )

    return jsonify(
        response.json()
    ), response.status_code


# GET PRODUCT BY ID
@product_bp.route(
    "/products/<int:id>",
    methods=["GET"]
)
@token_required
@role_required("ADMIN", "USER")
def get_product(id):
    response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products/{id}"
    )

    return jsonify(
        response.json()
    ), response.status_code


# UPDATE PRODUCT
@product_bp.route(
    "/products/<int:id>",
    methods=["PUT"]
)
@token_required
@role_required("ADMIN")
def update_product(id):
    response = requests.put(
        f"{PRODUCT_SERVICE_URL}/products/{id}",
        json=request.json
    )

    return jsonify(
        response.json()
    ), response.status_code


# DELETE PRODUCT
@product_bp.route(
    "/products/<int:id>",
    methods=["DELETE"]
)
@token_required
@role_required("ADMIN")
def delete_product(id):
    response = requests.delete(
        f"{PRODUCT_SERVICE_URL}/products/{id}"
    )

    return jsonify(
        response.json()
    ), response.status_code