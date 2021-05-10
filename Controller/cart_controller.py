from flask import Blueprint, Flask, request, json, Response
from Model.cart_model import Cart
from database import get_db_session
from sqlalchemy.orm import sessionmaker, relationship,backref, joinedload
#from app import app

cart_api = Blueprint('cart_api', __name__)

@cart_api.route('/cart')
def get_cart(): 
  s = get_db_session()
  carts = s.query(Cart)
  print(carts)
  return Response(json.dumps([d.to_dict() for d in carts]), status=200, mimetype='application/json')

@cart_api.route('/cart/<int:id>')
def get_cart_by_id(id): 
  print('==>', id)
  s = get_db_session()
  carts = s.query(Cart).filter(Cart.id == id)
  print('==>', carts.count())
  if (carts.count() > 0):
    cart = carts.one()
    print(cart.to_dict())
    return Response(json.dumps(cart.to_dict()), status=200, mimetype='application/json')
  
  return Response('No se encontraron carritos', status=200, mimetype='application/json')

@cart_api.route('/cart', methods=['POST'])
def create_cart(): 

    print('==>', request.form.get('product_id', ''))
    print('==>', request.form.get('user_id', ''))
    if not 'product_id' in request.form:
        return Response('product_id is missing', 400)

    if not 'user_id' in request.form:
        return Response('user_id is missing', 400)

    if not 'created' in request.form:
        return Response('created is missing', 400)

    product_id = request.form.get('product_id', '')
    user_id = request.form.get('user_id', '')
    created = request.form.get('created', '')
    cart = Cart(product_id,user_id, created)

    s = get_db_session()
    s.add(cart)
    s.commit()

    return Response('cart created', 201)

@cart_api.route('/carts', methods=['POST'])
def create_list_carts(): 
  return 2+2

@cart_api.route('/carts')
def get_list_carts(): 
  return 2+2

@cart_api.route('/cart', methods=['PATCH'])
def update_cart(): 
    return 2+2

@cart_api.route('/cart', methods=['DELETE'])
def delete_cart(): 
    return 2+2