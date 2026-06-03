from flask import Blueprint, jsonify, request
from models.order_model import Order, db
import requests
order_bp = Blueprint('orders', __name__)
# ---------------------------------------------------
# GET ALL ORDERS
# ---------------------------------------------------
@order_bp.route('/orders', methods=['GET'])
def get_orders():
   orders = Order.query.all()
   result = []
   for o in orders:
       result.append(o.to_dict())
   return jsonify(result)

# ---------------------------------------------------
# CREATE ORDER
# ---------------------------------------------------
@order_bp.route('/orders', methods=['POST'])
def create_order():
   data = request.get_json()
   product_id = data['product_id']
   quantity = data['quantity']
   # -----------------------------------------------
   # Call Product Service
   # -----------------------------------------------
   response = requests.get(
       f'http://127.0.0.1:5000/products/{product_id}'
   )
   # Product Not Found
   if response.status_code != 200:
       return jsonify({
           'error': 'Product not found'
       }), 404
   # Product Data
   product_data = response.json()
   # -----------------------------------------------
   # Create Order
   # -----------------------------------------------
   order = Order(
       product_id=product_id,
       quantity=quantity
   )
   db.session.add(order)
   db.session.commit()
   return jsonify({
       'message': 'Order created successfully',
       'order': {
           'id': order.id,
           'product_id': product_id,
           'product_name': product_data['name'],
           'price': product_data['price'],
           'quantity': quantity,
           'total_amount': product_data['price'] * quantity
       }
   }), 201