colores = ['azul','negro','amarillo','purpura']
misc = ['eduardo', 18, False, 14.5, '2015-04-14', ['1',2,3]]
#imprimir la primera posicion
print(colores[1])
#imprimir la ultima posicion d ela lista
print(colores[len(colores)-1])
print(colores[-1])
#Imprimir desde la 0 hasta la <2
print(colores[0:2])
#imprimir desde la posicion 1 hasta el final
print(colores[1:])

colores2 =colores[:]
colores2[0] = "violeta"
print(colores)

nombre = "Juanito"
print(nombre[1])
# solamente se puede usar las osiciones de una variable STR para leer mas no para modificar su contenido

colores.append('indigo')
print(colores)

#metodo para eliminar un valor

colores.remove("azul")
print(colores)
#el metodo pop ademas de eliminar, lo podemos almacenar en una variable
colore_eliminado = colores.pop(0)
print(colores)
print(colore_eliminado)

# metodo para resetear toda la lista y dejarla en blanco
colores.clear()
print(colores)

# TUPLAS => coleccion de elementos ordenada NO SE PUEDE MODIFICAR LUEGO DE SU CREACION
notas = [14, 16, 17, 11, 5, 1, 5, 5, 5]
print(notas[0])
print(notas[-1])

print(len(notas))
#cantidad de elementos de la tupla notas es 6 elemntos
print("la cantidad de elementos de la tupla notas es {} elementos".format(len(notas)))
print(f"la cantidad de elementos de la tupla notas es {len(notas)} elementos")

#ver si hay elemntos repetidos en una tupla
print (notas.count(5))

#CONJUNTOS => coleccion de elemntos DESORDENADA, osea que una vez creemos no podemos acceder a sus posiciones ya que se ordenaran aleatoreamente
estaciones = {"VERANOS", "OTOÑO", "PRIMAVERA", "INVIERNO"}
print(estaciones)
estaciones.add("OTOÑOVERANO")
# el metodo in sirve para validar si un valor esta dentro de una coleccion de datos 
print("OTOÑOVERNAO" in estaciones)

#DICCIONARIOS => coleccion de elemntos que estan INDEXADOS  , que nosotros manejamos el nombre de su llave
persona = {
    'id' : 1,
    'nombre': 'Aldito',
    "relacion": "Soltero",
    "fecha_nacimiento": "1992/08/04",
    "hobbies": [
        {
            "nombre":"futbol",
            "conocimiento": "Intermedio"
        },
        {
            "nombre": "Drones",
            "conocimiento": "Basico"
        }
    ]
}
print(persona['nombre'])
print(persona["hobbies"][0]['conocimiento'])
persona['apellido'] = "Martinez"

#para eliminar 


libro = {
    "nombre": "Harry Potter",
    "autor": "J.K. Rowling",
    "editorial": "Blablabla",
    "año": 2018,
    "idiomas": [
        {
            "nombre": "portuges"
        },
        {
            "nombre": "ingles",
            "nombre": "ingles britanico"
        },
        {
            "nombre": "frances"
        },
        {
            "nombre": "aleman"
        },
    ],
    "calificacion": 5,
    "imdb": "00asd12-asd878-a4s5d4a5-a45sd4a5sd",
    "tomos": ("La piedra filosofal", "La camara secreta", "El vuelo del fenix")
}

# EJERCICIO 1
# devolver el autor del libro
print(libro["autor"])
# EJERCICIO 2
# devolver el segundo tomo
print(libro["tomos"][1])
# EJERCICIO 3
# devolver la cantidad de idiomas del libro
print(len(libro["idiomas"]))
# EJERCICIO 4
# indicar si esta o no esta el idioma ruso
print(libro["idiomas"]["nombres"])