from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# ---------------------------------------------------
# Order Model
# ---------------------------------------------------
class Order(db.Model):
   id = db.Column(
       db.Integer,
       primary_key=True
   )
   product_id = db.Column(
       db.Integer,
       nullable=False
   )
   quantity = db.Column(
       db.Integer,
       nullable=False
   )
   # Explicit Constructor
   def __init__(self, product_id, quantity):
       self.product_id = product_id
       self.quantity = quantity
   # Convert Object → Dictionary
   def to_dict(self):
       return {
           'id': self.id,
           'product_id': self.product_id,
           'quantity': self.quantity
       }