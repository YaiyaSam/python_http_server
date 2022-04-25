from flask import Flask
from flask_restful  import Resource, Api, reqparse
from flask_mysqldb import MySQL
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

app.config['db_host'] = 'localhost:3306'
app.config['db_user'] = 'root'
app.config['db_password'] = 'Root@1234'
app.config['db_database'] = "httpServer"

mysql = MySQL(app)
# cursor = mysql.connection.cursor() 

class Users(Resource):
    pass

class Profile(Resource):
    pass

api.add_resource(Users,'/users')
api.add_resource(Profile, '/profile')

if __name__ == '__main__':
    app.run()