from flask import Blueprint, Flask, request, json, Response
from Model.user_model import User
from database import get_db_session
from sqlalchemy.orm import sessionmaker, relationship,backref, joinedload
#from app import app

user_api = Blueprint('user_api', __name__)

@user_api.route('/user')
def get_user(): 
  s = get_db_session()
  users = s.query(User)
  print(users)
  return Response(json.dumps([d.to_dict() for d in users]), status=200, mimetype='application/json')

@user_api.route('/user/<int:id>')
def get_user_by_id(id): 
  print('==>', id)
  s = get_db_session()
  users = s.query(User).filter(User.id == id)
  print('==>', users.count())
  if (users.count() > 0):
    user = users.one()
    print(user.to_dict())
    return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')
  
  return Response('No se encontraron usuarios', status=200, mimetype='application/json')

@user_api.route('/user', methods=['POST'])
def create_user(): 

  print('==>', request.form.get('username', ''))
  print('==>', request.form.get('firstname', ''))
  print('==>', request.form.get('lastname', ''))
  print('==>', request.form.get('password', ''))

  username = request.form.get('username', '')
  if username == '':
    return Response('{"error-message":"username cannot be empty"}', status=400, mimetype='application/json')
  firstname = request.form.get('firstname', '')
  lastname = request.form.get('lastname', '')
  password = request.form.get('password', '')
  
  if password == '':
    return Response('{"error-message":"password cannot be empty"}', status=400, mimetype='application/json')

  user = User(username, firstname, lastname, password)

  s = get_db_session()
  s.add(user)
  s.commit()

  return Response('user created', 201)

@user_api.route('/users', methods=['POST'])
def create_list_users(): 
  return 2+2

@user_api.route('/users')
def get_list_users(): 
  return 2+2

@user_api.route('/user', methods=['PATCH'])
def update_user(): 
    return 2+2

@user_api.route('/user', methods=['DELETE'])
def delete_user(): 
    return 2+2