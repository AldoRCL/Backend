# crear una clase Persona en la cual se guarden su nombre, fecha nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente
#En la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.


class Persona:
    def __init__(self,nombre,fecha_nac,nacionalidad,dni):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.nacionalidad = nacionalidad
        self.dni = dni
    def saludar(self):
        print("Hola me llamo {}".format(self.nombre))


class Docente(Persona):
    def __init__(self,nombre,fecha_nac,nacionalidad,dni,cts,seguro_social):
        super().__init__(nombre,fecha_nac,nacionalidad,dni)
        self.cts = cts
        self.seguro_social = seguro_social

    def mostrar_cts(self):
        print("Su cta cts es {}".format(self.cts))


class Alumno(Persona):
    def __init__(self,nombre,fecha_nac,nacionalidad,dni,cursos):
        super().__init__(nombre,fecha_nac,nacionalidad,dni)
        self.cursos = cursos

# ahora en base a esas clases se pide hacer los siguientes cambios,
# 1. crear un getter y un setter para mostrar los cursos de los alumnos
# 2. hacer que el cts sea un atributo privado y que solamente se pueda ingresar su valor mediante el metodo ingresar_cts
# 3. que la nacionalidad tenga un valor predeterminado de PERUANO si es que no se asigna uno


