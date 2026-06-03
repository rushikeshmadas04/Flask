from flask import Blueprint, jsonify, request

from models.product_model import Product, db

product_bp = Blueprint(

    'product_bp',

    __name__

)

# -----------------------------------

# GET ALL PRODUCTS

# -----------------------------------

@product_bp.route('/products', methods=['GET'])

def get_products():

    products = Product.query.all()

    result = []

    for p in products:

        result.append(p.to_dict())

    return jsonify(result)

# -----------------------------------

# CREATE PRODUCT

# -----------------------------------

@product_bp.route('/products', methods=['POST'])

def create_product():

    data = request.get_json()

    product = Product(

        name=data['name'],

        price=data['price']

    )

    db.session.add(product)

    db.session.commit()

    return jsonify({

        'message': 'Product created successfully'

    }), 201


@product_bp.route('/products/<int:id>',methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())