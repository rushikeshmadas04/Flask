from flask import (
    Blueprint,
    jsonify,
    request
)

import requests

from config import (
    ORDER_SERVICE_URL
)

from middleware.jwt_middleware import (
    token_required
)

from middleware.authorization import (
    role_required
)

order_bp = Blueprint(
    "order_bp",
    __name__
)


# GET ORDERS
@order_bp.route(
    "/orders",
    methods=["GET"]
)
@token_required
@role_required("ADMIN", "USER")
def get_orders():

    response = requests.get(
        f"{ORDER_SERVICE_URL}/orders"
    )

    return jsonify(
        response.json()
    ), response.status_code


# CREATE ORDER
@order_bp.route(
    "/orders",
    methods=["POST"]
)
@token_required
@role_required("ADMIN", "USER")
def create_order():

    response = requests.post(
        f"{ORDER_SERVICE_URL}/orders",
        json=request.json
    )

    return jsonify(
        response.json()
    ), response.status_code