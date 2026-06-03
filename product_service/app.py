from flask import Flask
from models.product_model import db
from routes.product_routes import product_bp
# -----------------------------------
# Flask App
# -----------------------------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# -----------------------------------
# Initialize SQLAlchemy
# -----------------------------------
db.init_app(app)
# -----------------------------------
# Register Blueprint
# -----------------------------------
app.register_blueprint(product_bp)
# -----------------------------------
# Create Tables
# -----------------------------------
with app.app_context():
   db.create_all()
# -----------------------------------
# Run App
# -----------------------------------
if __name__ == '__main__':
   app.run(port=5000)