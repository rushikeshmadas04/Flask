from flask import Flask

from models.order_model import Order, db

from routes.order_routes import order_bp

import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(

    order_bp,

    url_prefix='/api'

)

with app.app_context():

    db.create_all()

if __name__ == '__main__':

    app.run(debug=True,port=5001)
 