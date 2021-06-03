from Config.conexion_bd import base_de_datos
from sqlalchemy import Column, types,orm


class PostreModel(base_de_datos.Model):
    #para cambia el nombre de la tabla en la base de datos
    __tablename__ = "postres"

    postreId = Column(name='id', primary_key=True,
                      autoincrement=True, unique=True, type_=types.Integer)

    postreNombre = Column(name='nombre',type_=types.String(length=45))
    postrePorcion = Column(name='porcion', type_=types.String(length=25))
    #rlationship isrve para indicar todos los "hijos" que puede tener ese modelo (todas sus FK)
    ##el backref crearea un atributo virtual en el model del hijo (preparacio ) para que pueda acceder a todo el objeto de PotreModel sin la necesidad de hacer una sub consulta (creara un join cuando sea necesario )
    #lazy => define cuando SQLAlchemy va a cargar la data adyacente de la base de datos
    #Truer / 'select' => cargara osod los datos adyacentes
    #False / 'join' => solamente cargara cuando sea necesario (cuando se utilicen dichos datos)
    #'subquery' => trbajara los datos PERO en una sub consulta
    #'dynamic' => en este se pueden agregar filtros adicionales.SQLAlchemy devolvera otro objeto dentro de la clase
    preparaciones = orm.relationship('PreparacionModel',backref='postrePreparaciones',lazy=True)

    def __init__(self, nombre, porcion):
        self.postreNombre= nombre
        self.postrePorcion= porcion
    def __str__(self):
        return "El nombre es %s" % self.postreNombre
    def save(self):
        base_de_datos.session.add(self)

        base_de_datos.session.commit()

        #base_de_datos.session.close()

    def json(self):
        return{
            "postreid":self.postreId,
            "postreNombre":self.postreNombre,
            "psotrePorcion": self.postrePorcion
        }