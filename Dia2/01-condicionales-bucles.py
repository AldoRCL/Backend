"""#Input es el petodo que existe para ingresar datos por el terminal
edad = input("Ingresa tu Edad: ")
print(type(edad))
edadEntero = int(edad)
#print(edadEntero)
# \n => salto de linea
# \t => tabulacion
#number = int(input("Ingresa un numero: \n"))
#print(type(number))

#CONDICION
restriccion_edad = 18
if edadEntero >= restriccion_edad and edadEntero < 65:
    print("Eres mayor de edad, ya puedes viajar")
elif edadEntero>=65 :
    print("Puedes irte de crucero")
else:
    print("Eres menor de edad, aun no puedes hacer nada :( ")


#OPERADOR TERNARIO
#es una forma de hacer una validacion en una sola linea de codigo con uno o varios condicionales en el if
respuesta = "ERES MAYOR DE EDAD" if(edadEntero >= 18) else "ERES MENOR DE EDAD"

print(respuesta)

number = -1
if number > 0:
    print("Eres Positivo")
elif number < 0 :
    print("Eres Negativo")
else:
    print("El 0 no es positivo ni negativo")

# BUCLES
# FOR =>
meses = ["ENERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", ]

for mes in meses:
    print(mes)

for numero in range(1, 5, 1):
    print(numero)

diccionario = {
    "nombre": "Aldito",
    "apellido": "Cotrina"
}
for llave in diccionario:
    print(diccionario[llave])

# ingresar una tupla o diccionario
numeros = [1, -5, 8, -14, 16, 20]
for numero in numeros:
    print(numero)

for segundo in range(10):
    print("El segundo es", segundo)

positivo = 0
negativo = 0
numeros = [1, -4, 5, -14, -16, -50, 6, -100]
for compara in numeros:
    if compara > 0:
        positivo+= 1
    else:
        negativo+= 1

print(f"Hay {positivo} numeros positivos")
print(f"Hay {negativo} numeros negativos")

"""
# break => hace que el bucle finalice
for i in range(10):
    print(i)
    if i == 5:
        break

# continue => salta la iteracion actual y no permite que el resto del codigo se ejecute
for i in range(10):
    if i == 5:
        continue
    print(i)

numeros = [1, 2, 5, 9, 12, 15, 10, 34, 867, 67]
# indicar cuantos de ellos son multiplos de 3 y de 5, ademas, si hay un multiplo de 3 y de 5 no contabilizarlo
mul3 = 0
mul5 = 0
otro =0
for itera in numeros:
    if (itera%3) == 0 and (itera%5) != 0:
        mul3+=1
        print(itera)
    elif(itera%5) == 0 and (itera%3) != 0:
        mul5+=1 
    else:
        otro+=1
print(f"Multiplos de 3 hay :{mul3}")
print(f"Multiplos de 5 hay :{mul5}")
print(f"Otros multiplos hay: {otro}")

edad = 25
while edad > 18:
    print(edad)
    edad -= 1
# ingresar por teclado 3 nombres y de acuerdo a ello indicar cuantos pertenecen a la siguiente lista de personas inscritas
inscritos = ["raul", "pedro", "maria", "roxana", "margioret"]

nombre1 = input("Ingresa el primer nombre")
nombre2 = input("Ingresa el segundo nombre")
nombre3 = input("Ingresa el tercero nombre")

