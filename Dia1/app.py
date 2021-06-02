from flask import Flask, request
# Para usar las variables declaradas en el archivo .env
from dotenv import load_dotenv
from os import environ

from flask_sqlalchemy import model
from Config.conexion_bd import base_de_datos
from flask_restful import Api
from controllers.postre import PostresController
from models.postres import PostreModel
from models.preparacion import PreparacionModel
from models.ingredientes import IngredienteModel
from models.receta import RecetaModel

load_dotenv()

app = Flask(__name__)
api = Api(app)
# https://docs.sqlalchemy.org/en/14/core/engines.html
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
# dialect://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

base_de_datos.init_app(app)


base_de_datos.create_all(app=app)
@app.route("/")
def initial_controller():
    return {
        "message": "Bienvenido a mi API de RECETAS DE POSTRES 🎂"
    }

api.add_resource(PostresController, "/postres")

if __name__ == '__main__':
    app.run(debug=True)