from flask import Flask, request,jsonify
from flask_mysqldb import MySQL
#esto sirve parq ue si tenemos un archivo .env jale todas las variables como si fueran varuiables de entorno
from dotenv import load_dotenv
from os import environ
load_dotenv()

app = Flask(__name__)
app.config['MYSQL_HOST'] = environ.get("HOST")
app.config['MYSQL_USER'] = environ.get("USER")
app.config['MYSQL_PASSWORD'] = environ.get("PASSWORD")
app.config['MYSQL_DB'] = environ.get("DATABASE")
app.config['MYSQL_PORT'] = int(environ.get("PORT"))

#Creamos un ainstantcioa de la claser MYSQL y le pasamos a su constructor la configuracion

mysql = MySQL(app)

@app.route("/alumnos")
def  gestion_alumnos():
    #Primero creo mi cursor que se conectara a la db
    cur = mysql.connection.cursor()
    #Registro la sentencia ya sea un DDL o DML
    cur.execute("SELECT * FROM ALUMNOS")
    #Capturo la informacin a partir de la consulta
    data = cur.fetchall()
    return{
        "data": data
    }


app.run(debug=True)