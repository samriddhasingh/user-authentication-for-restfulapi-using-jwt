
from role_api.models.user import verify_user,final_data
from role_api.utils.jwt_utils import create_access_tokens
from flask_jwt_extended import jwt_required, get_jwt_identity


def logins(username,password):

    valid_user=verify_user(username,password)
    token=create_access_tokens(username)
    return valid_user,token

def get_data():
    current_user=get_jwt_identity()
    data=final_data(current_user)
    return {'message': f' {data}'}, 200

    