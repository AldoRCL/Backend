from flask import Flask, request
from flask.wrappers import Request


print(__name__)
app = Flask( __name__ )

@app.route('/')
def inicio():
    print("Me hicieron un llamado")
    return "SALUDOS DESDE MI API"
@app.route('/productos', methods = ['GET','POST'])
def gestion_productors():
    print(request.method)

    #request.get_json()  Podemos ver la informacion que me esta brindando el frontend mediante el body
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return{
            "message" : "Producto creado exitosamente"
        }
    elif request.method == 'GET':
        return{ 
            "message" : "Estos son los productos registrados"
        }

    return{
        "message": "Saludos desde el controlador de productos"
    }

app.run(debug = True)