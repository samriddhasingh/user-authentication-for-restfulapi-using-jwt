
from flask import Blueprint,request,json
from role_api.controllers.auth_controller import logins,get_data
from flask_jwt_extended import jwt_required,get_jwt_identity

auth =Blueprint('auth',__name__)
api=Blueprint('api',__name__)


@auth.route('/login',methods=['POST'])
def login():

    data=request.get_json()
    username=data.get('username')
    password=data.get('password')
    valid_user,token=logins(username,password)

    return token

@api.route('/data',methods=['GET'])
@jwt_required()
def data_route():
    return get_data()



