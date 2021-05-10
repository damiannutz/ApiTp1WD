from flask import Blueprint, Flask, request, json, Response
from Model.user_model import User
from Model.product_model import Product
from database import get_db_session
from sqlalchemy.orm import sessionmaker, relationship,backref, joinedload
#from app import app

product_api = Blueprint('product_api', __name__)

@product_api.route('/product')
def get_product(): 
  s = get_db_session()
  products = s.query(Product)
  print(products)
  return Response(json.dumps([d.to_dict() for d in products]), status=200, mimetype='application/json')

@product_api.route('/product/<int:id>')
def get_product_by_id(id): 
  print('==>', id)
  s = get_db_session()
  product = s.query(Product).filter(Product.id == id).one()
  print(product.to_dict())
  return Response(json.dumps(product.to_dict()), status=200, mimetype='application/json')

@product_api.route('/product', methods=['POST'])
def create_product(): 
  print('==>', request.form.get('name', ''))
  print('==>', request.form.get('image', ''))
  if not 'name' in request.form:
    return Response('name is missing', 400)

  name = request.form.get('name', '')
  if name == '':
    return Response('{"error-message":"name cannot be empty"}', status=400, mimetype='application/json')
  image = request.form.get('image', '')
  description = request.form.get('description', '')
  price = request.form.get('price', '')
  stock = request.form.get('stock', '')

  product = Product(name, description, image, price,stock )

  s = get_db_session()
  s.add(product)
  s.commit()

  return Response('Product created', 201)

@product_api.route('/products', methods=['POST'])
def create_list_products(): 
  return 2+2

@product_api.route('/products')
def get_list_products(): 
  return 2+2

@product_api.route('/product', methods=['PATCH'])
def update_product(): 
    return 2+2

@product_api.route('/product', methods=['DELETE'])
def delete_product(): 
    return 2+2