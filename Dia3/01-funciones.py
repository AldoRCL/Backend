# una funcion es un bloque de codigo que se puede reutilizar cuantas veces sea necesario

numer1 = 10
numer2 = 20
sumatoria = numer1 + numer2

def saludar():
    """Funcion que te saluda cordialmente"""
    print ("Hola amigos buena tardes")

saludar()
print("Ya es algo tarde")

# las funciones TAMBIEN pueden recibir parametros que son variales que solamente existiran dentro de las mismas

def saludarConNombre(nombre):
    """Funcion que recibe un nombre e imprime un saludo con ese nombre"""
    print (f"Hola {nombre} buenas tardes")

saludarConNombre("Aldo")

def saludoOpcionale (nombre=None):
    print(f"Hola {nombre} como estas")

saludoOpcionale("Fernando")

#si nosotros queremos recibir parametros obligatoriamente y algunos opcionalmente, los parametros opcionales SIEMPRE tieen que ir al final de la declaracion
def registro(correo, nombre=None ):
    print("Registro Exitoso")

registro("pepe@yopmail.com")

# funcion que reciba dos numeros y si la sumatoria de ambos es par indicar su mitad y si es impar, retornar el resultado de la sumatoria

number1 = int(input("Ingresa un numero: \n"))
number2 = int(input("Ingresa otro numero: \n"))

def funti (a,b):
    sum= a+b
    if((sum)%2==0):
        print(f"El numero es par y su mitad es {sum}")
    else:
        print(f"Su numero es impar y su suma es ¨{sum}")

funti(number1,number2)

#el parametro *args es una lista dinamica de elementos para recibir un numero ilimitado de valores
def inscritos(*args):
    print(args)

inscritos("Eduardo","Carlos","Ricardo","Gmelina","Jesus")
inscritos(1, False, "Eduardo", 12.5)


def tareas(nombre,*args):
    print(nombre)
    print(args)

tareas("TAREA BACKEND", "crear un archivo python",
       "hacer la suma de 3 numeros", "hacer la serie fibonacci")
# definir una funcion para que reciba una N cantidad de alumnos y que indique cuantos fueron aprobados y cuandos desaprobaron

def alumnos(*args):
    aprobados = 0
    desaprobados = 0
    total = len(args)
    for alumno in args:
        print (alumno["nota"])
        if(alumno["nota"] > 10):
            aprobados+=1
    pass

alumnos({"nombre": "Eduardo", "nota": 7},
        {"nombre": "Fidel", "nota": 16},
        {"nombre": "Raul", "nota": 18},
        {"nombre": "Marta", "nota": 20},
        {"nombre": "Juliana", "nota": 14},
        {"nombre": "Fabiola", "nota": 16},
        {"nombre": "Lizbeth", "nota": 15})


