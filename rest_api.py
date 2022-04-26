from flask import Flask, request
from flask_restful  import Resource, Api
from flask_mysqldb import MySQL
import pandas as pd
from urllib.request import urlopen
import json

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root@1234'
app.config['MYSQL_DB'] = 'httpServer'

mysql = MySQL(app)
    
# -----------------you cannot call a cursor outside of a request function----------------
#   cursor = mysql.connection.cursor()  

class Users(Resource):

    def get(self):
        url = "https://jsonplaceholder.typicode.com/users"
        response = urlopen(url)
        data = json.loads(response.read())
        return {'data':data}, 200
 




# --------------------link the classes with the endpoints---------------------------

api.add_resource(Users,'/users')



# ------------------------run the application----------------------------------
if __name__ == '__main__':
    app.run()