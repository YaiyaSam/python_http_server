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
 

    def post(self):
        url = "https://jsonplaceholder.typicode.com/users"
        response = urlopen(url)
        data = json.loads(response.read())
        
        id = request.args.get("name")
        name = request.args.get("id")
        username = request.args.get("username")

        new_data = {
            'id':  id,
            'name': name,
            'username': username
        }

        data.append(new_data)
        return {'data':data}, 200

# ---------------------------------this did not work-------------------------------------

        # parser = reqparse.RequestParser() 
        
        # parser.add_argument('id', required=False)
        # parser.add_argument('name', required=False)
        # parser.add_argument('username', required=False)
        
        # args = parser.parse_args()  # parse arguments to dictionary
        
        # print(args)
        
        # new_data = {
        #     'id': args['id'],
        #     'name': args['name'],
        #     'username': args['username']
        # }
        # data = data.append(new_data, ignore_index=True)
        # new_data = json.dumps(new_data)
        # data.update(new_data)
        # print(args['id'])
        # return {'data':data}, 200


class Profile(Resource):

    def get(self):
    
       cursor = mysql.connection.cursor()  
       cursor.execute('''SELECT * FROM profile''')
       result = cursor.fetchall()
       cursor.close()
       
       return result, 200


    def post(self):

        cursor = mysql.connection.cursor()
        firstName = request.args.get("firstName")
        lastName = request.args.get("lastName")
        email = request.args.get("email")

        cursor.execute('''INSERT INTO profile (firstName,lastName,email) VALUES(%s,%s,%s)''',(firstName,lastName,email))
        mysql.connection.commit()
        cursor.close()

        return "Profile added!!", 200


# --------------------link the classes with the endpoints---------------------------

api.add_resource(Users,'/users')
api.add_resource(Profile, '/profile')


# ------------------------run the application----------------------------------
if __name__ == '__main__':
    app.run()