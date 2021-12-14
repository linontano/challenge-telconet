from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource, abort
import mysql.connector as db
from mysql.connector import Error

app = Flask(__name__)
cors =CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

def connectionMysql():
  config = {
    'user': 'challenge_admin',
    'password': 'challenge12345',
    'host': 'mysql',
    'database': 'challenge_telconet',
    'port': '3306'
  }
  try:
    connection = db.connect(**config)
    if connection.is_connected():
      return connection
    else:
      return False
  except Error as e:
    return False
def validateNetwork(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
      for part in parts:
        if not isinstance(int(part), int):
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    except ValueError:
      return False
    return True
def getRoutes(network):
    table_name = "bgp_ipv4_unicast"
    if not validateNetwork(network):
        abort(400)
    conn = connectionMysql()
    if conn == False:
        abort(503)
    try:
        query = "SELECT b.OUTPUT, b.TIME_EXECUTION FROM {tablename}  as b WHERE b.NETWORK_INPUT=%s ORDER BY b.TIME_EXECUTION DESC".format(tablename=table_name)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (network, ))
        response = cursor.fetchone()
        if response is None:
            abort(404, message="No existe esa red en nuestra base de datos")
        return {"TIME": str(response["TIME_EXECUTION"]), "OUTPUT": str(response["OUTPUT"], 'UTF-8')}
    except Error as e:
        abort(503)

class Route(Resource):
    @cross_origin()
    def get(self, network):
        return getRoutes(network)

api.add_resource(Route, "/api/routes/<string:network>")
if __name__ =="__main__":
    app.run(debug=True)