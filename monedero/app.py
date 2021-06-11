from flask import Flask, request, send_file
from flask_restful import Api
from controllers.usuario import RegistroController
from controllers.movimiento import MovimientosController
from models.sesion import SesionModel
from os import environ, path, remove
from dotenv import load_dotenv
from config.conexion_bd import base_de_datos
from flask_jwt import JWT
from config.seguridad import autenticador, identificador
from config.custom_jwt import manejo_error_JWT
from datetime import timedelta
#sirve para que el nombre dle archivo que manda el cliente de guardarte, lo valide y evite que se guarde con caracteres espaeciales que puedne malograr el funcionamiento de la api o guardar de una forma incorrecta
from werkzeug.utils import secure_filename
from uuid import uuid4
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'claveSecreta'
# para modificar la fecha de caducidad de la token, su valor x default es 600 segundos
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1)
# para modificar el endpoint del login
app.config['JWT_AUTH_URL_RULE'] = '/login'
# para modificar la llave del username
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
# para modificar la llave del password
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pass'
# Si estamos subiendo archivos, para poner un tope usaremos la variable MAX_CONTENT_LENGTH
# 1 byte  * 1024 => 1Kb * 1024 => 1 Mb * 1024 => 1 Gb
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

jsonwebtoken = JWT(app=app, authentication_handler=autenticador,
                   identity_handler=identificador)


jsonwebtoken.jwt_error_callback = manejo_error_JWT
base_de_datos.init_app(app)
# base_de_datos.drop_all(app=app)
base_de_datos.create_all(app=app)

EXTENSIONES_PERMITIDAS = ['png', 'jpg', 'pdf','jpeg']


def archivos_permitidos(filename):
    # rsplit puede recibir dos parametros, el primer parametro es el caracter a dividir y el segundo opcional es el que especifica en cuantas partes debe de ser dividido
    return '.' in filename and filename.rsplit('.', 1)[-1].lower() in EXTENSIONES_PERMITIDAS


api = Api(app)


@app.route("/subirArchivo", methods=['POST'])
def subir_archivo():
    print(request.files)
    archivo = request.files['archivo']
    # Solamente registrar los archivos que son JPG, PNG y PDF
    # para saber el nombre del archivo
    print(archivo.filename)
    # para saber el tipo de archivo
    print(archivo.mimetype)  # image/jpg image/png  application/vnd.rar
    if archivos_permitidos(archivo.filename):
        # primero saco el formato del archivo
        formato_archivo = archivo.filename.rsplit(".", 1)[-1]
        # genero un uuid y le agrego la extension
        nombre_archivo = str(uuid4())+'.'+formato_archivo
        # aca validara que no existan caracteres especial que puedan romper el funcionamiento de mi api
        nombre_archivo = secure_filename(nombre_archivo)
        archivo.save(path.join("multimedia", nombre_archivo))
        return {
            "success": True,
            "content": request.host_url+'media/'+nombre_archivo,
            "message": "archivo registrado correctamente"
        }
    else:
        return {
            "success": False,
            "content": None,
            "message": "Archivo no permitido"
        },400

@app.route("/media/<string:nombre>", methods=['GET'])
def devolverArchivo(nombre):
    try:
        return send_file(path.join("multimedia", nombre))
    except:
        return send_file(path.join("multimedia", "not_found.jpeg")),404

@app.route("/eliminarArchivo/<string:nombre>", methods=['DELETE'])
def eliminar_archivo(nombre):

    try:
        remove(path.join("multimedia",nombre))
        return{
            "success":True,
            "content":None,
            "message":"Archivo eliminado exitosamente"
        }
    except:
        return{
            "success":False,
            "content":None,
            "message":"Archivo no encontrado"
        },404



api.add_resource(RegistroController, "/registro")
api.add_resource(MovimientosController, "/movimientos")

if __name__ == '__main__':
    app.run(debug=True)