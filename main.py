from flask import Flask
from flask_jwt_extended import JWTManager
from role_api.views.auth_view import api,auth


app= Flask(__name__)

app.config['JWT_SECRET_KEY']="samriddha"
jwt=JWTManager(app)



app.register_blueprint(auth)
app.register_blueprint(api)



if __name__ == '__main__':
    app.run(debug=True)

from role_api.controllers import *