from flask_jwt_extended import create_access_token,decode_token

from datetime import timedelta


def create_access_tokens(identity):
    print("database")
    expires=timedelta(days=1)
    token=create_access_token(identity=identity, expires_delta=expires)
    return token

def decode_jwt_token(token):
    try:
        payload = decode_token(token)
        return payload
    except Exception as e:
        return None

