from flask import Flask, request,jsonify
from flask_mysqldb import MySQL
#esto sirve parq ue si tenemos un archivo .env jale todas las variables como si fueran varuiables de entorno
from dotenv import load_dotenv
from os import environ
import math
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
    alumnos = cur.fetchall()
    alumnos_dict =[]
    for alumno in alumnos:
        alumno_dict = {
            "id": alumno[0],
            "matricula":alumno[1],
            "nombre":alumno[2],
            "apellido":alumno[3],
            "localidad":alumno[4],
            "fecha_nacimiento":alumno[5]
        }
        alumnos_dict.append(alumno_dict)
    return{
        "data": alumnos_dict
    }

@app.route("/alumnos-paginados", methods=['GET'])
def alumnos_paginados():
    print(request.args)
    if(request.args.get('pagina')and request.args.get('porPagina')):
        porPagina = int(request.args.get('porPagina'))
        pagina = int(request.args.get('pagina'))
        limit = porPagina
        offset = (pagina - 1) * porPagina
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM alumnos LIMIT %s OFFSET %s" %(limit, offset))
        resultado = cur.fetchall()
        print(len(resultado))
        print(resultado)
        #Ahora lo hacemos los datos de paginacion
        cur.execute("SELECT count(*) FROM alumnos")
        total = int(cur.fetchone()[0])

        itemsPorPagina = porPagina if total >= porPagina else total
        totalPaginas = math.ceil(total / itemsPorPagina)
        if pagina > 1:
            paginaPrevia = pagina - 1  if pagina <= totalPaginas else None
        else:
            paginaPrevia = None
        if totalPaginas > 1:
            paginaContinua = pagina + 1 if pagina < totalPaginas else None
        else:
            paginaContinua = None
        
    return{
        "data": resultado,
        "paginacion": {
            "total": total,#total de paginas
            "porPagina": itemsPorPagina,#pagina actual
            "paginaPrevia": paginaPrevia,#pagina precia
            "paginaContinua": paginaContinua, #pagians continua
            "totalPaginas": totalPaginas, #total de paginas
        }
    }
app.run(debug=True)