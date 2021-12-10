#######################################################
##### SCRIPT BGP - python scriptBGP.py <NETWORK> ######
#######################################################
import telnetlib
import sys
import mysql.connector as db
from mysql.connector import Error
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
def connectionMysql():
  config = {
    'user': 'challenge_admin',
    'password': 'challenge12345',
    'host': 'mysql',
    'database': 'challenge_telconet',
    'port': '3306'
  }
  try:
    print("Iniciando conexión MySQL a",config["database"],"...")
    connection = db.connect(**config)
    if connection.is_connected():
      return connection
    else:
      print("Ops, no se ha podido conectar al servidor MySQL")
      return False
  except Error as e:
    print("Error mientras se realizaba la conexión MySQL...", e)
    return False
def addData(conn,data,tablename):
  try:
    cursor = conn.cursor()
    query = """INSERT INTO {table} (NETWORK_INPUT, OUTPUT) VALUES (%s,%s)""".format(table=tablename)
    values = (data[0],data[1])
    cursor.execute(query, values)
    conn.commit()
    print("Contenido agregado con éxito")
    cursor.close()
  except db.Error as e:
    print(e)
  finally:
    if conn.is_connected():
      cursor.close()
def checkCreateTable(conn, tablename):
  try :
    query = """SELECT COUNT(*) 
              FROM information_schema.tables
              WHERE table_name = '{0}'
              """.format(tablename.replace('\'', '\'\''))
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchone()
    cursor.close()
    if records[0] != 1:
      #TABLE DOESNT EXISTS - CREATE TABLE
      print("Tabla no existe, creando tabla...")
      query = """CREATE TABLE {table} (
        id int(10) NOT NULL AUTO_INCREMENT,
        NETWORK_INPUT varchar(100) DEFAULT NULL,
        TIME_EXECUTION TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        OUTPUT BLOB,
        PRIMARY KEY (`id`))""".format(table=tablename)
      cursor = conn.cursor()
      cursor.execute(query)
      cursor.close()
    print("Tabla creada...")
    return True
  except db.Error:
    return False
#Datos de la conexión remota
command = "show bgp ipv4 unicast <ip>"
host = "route-server.he.net" 
username = "rviews"
password = "rviews"
tablename = "bgp_ipv4_unicast"
print("Iniciando conexión Telnet con enrutador", host,"...")
try:
  connection=False
  # network = input("Ingrese red: ")
  # while(not validateNetwork(network)):
  #   network = input("Ingrese una red válida: ")
  network = str(sys.argv[1])
  if (not validateNetwork(network)):
    raise Exception("No se ingresó una red válida")
  command = command.replace("<ip>",network)
  connection = telnetlib.Telnet(host)
  connection.read_until(b"Password: ")
  print("Validando credenciales...")
  connection.write(password.encode("ascii")+b"\n")
  connection.read_until(b"route-server> ")
  print("Ingresando comando...",command)
  connection.write(command.encode("ascii")+b"\n")
  connection.write(b"exit\n")
  response = connection.read_all().decode("ascii")
  #Guardar Data
  conn = connectionMysql()
  if conn:
    print("Saving data...")
    if (checkCreateTable(conn, tablename)):
      addData(conn,[network,response],tablename)
    else:
      print("Error, conexión fallida a base de datos. Intente nuevamente.")
    
except Exception as e :
  print(e)
  print("¡Ops! Algo ha pasado, inténtalo nuevamente más tarde")

finally:
  #Cierre de conexión
  print("Conexión finalizada")
  #client.close()
  if (connection):
    connection.close()