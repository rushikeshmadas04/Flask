from flask import Flask
from routes.auth_routes import (
   auth_bp
)
from routes.product_routes import (
   product_bp
)
from routes.order_routes import (
   order_bp
)
app = Flask(__name__)
app.register_blueprint(
   auth_bp
)
app.register_blueprint(
   product_bp
)
app.register_blueprint(
   order_bp
)
# Health Endpoint
@app.route("/health")
def health():
   print("Health Route HIT")
   return {
       "status": "UP"
   }

if __name__ == "__main__":
   app.run(
       host="0.0.0.0",
       port=9000,
       debug=True
   )