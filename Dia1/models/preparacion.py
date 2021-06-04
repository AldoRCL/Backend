from sqlalchemy.sql.schema import ForeignKey
from Config.conexion_bd import base_de_datos
from sqlalchemy import Column, types


class PreparacionModel(base_de_datos.Model):
    __tablename__ = "preparaciones"

    preparacionId = Column(name='id', type_ = types.Integer,
                            unique = True, autoincrement=True, primary_key=True)

    preparacionOrden = Column(name = 'orden', type_=types.Integer, nullable=False)
    

    preparacionDescripcion = Column(name = 'descripcion', type_ = types.Text, nullable = False)








    postre = Column(ForeignKey(column='postres.id',ondelete="CASCADE"),
                    name = 'postre_id',type_=types.Integer, nullable=False)

    def __init__(self, orden,descripcion, postre_id):
        self.preparacionOrden = orden
        self.preparacionDescripcion = descripcion
        self.postre = postre_id

    def save(self):
        base_de_datos.session.add(self)
        base_de_datos.session.commit()

    def json(self):
        return {
            "id": self.preparacionId,
            "orden": self.preparacionOrden,
            "descripcion": self.preparacionDescripcion,
            "postre": self.postre
        }