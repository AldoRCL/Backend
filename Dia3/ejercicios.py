# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****

#ancho = int(input(f"Ingrese el Ancho : \t"))
#largo = int(input(f"Ingrese el Largo : \t"))

#for j in range(0,largo):
#    for j in range(0,ancho):
#        print ("*", end="")
#    print("")


# Escribir una funcion que nosotros le ingresemos el lado de un hexagono y que lo dibuje
# Ejemplo:
# Lados: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****


n = int(input("Ingresa numero: "))
aste = 0
aste2 = 0
espacios = 0
validador = False

for i in range(0,(3*n)-2):
    
    if (n+aste)<=(3*n)-2:
        print ("*"*(n+aste), end="")
        print("")
        aste+=2
    aste2=aste
    
    if (n+aste)==(3*n)-2 :
        for i in range(1,n):
            print ("*"*(n+aste), end="")
            print("")
            validador = True
    
    if validador == True:
        for i in range(1,n):
            print ("*"*(n+aste2), end="")
            print("")
            aste-=2
    
    

"""
n = int(input("Ingresa numero: "))
c=0
for i in range(n      ):
    if n!=c : 
        espacios = n - i
        print(' ' * espacios + '*' * (n+(i+c)))
        c+=1
    else:
        for i in range(n):
            print ('*' * (n+(i+c)), end="")
"""

"""
n = int(input("Ingresa numero: "))
cont=n
vinit = n
for i in range(1,n) :
    for j in range(1,cont):
        print (" ", end="")
    for k in range(0,n):
         print ("*", end="")
    n+=2
    cont-=1
    print("",cont)

    if cont == 1:
        for j in range(vinit):
            for k in range(0,n):
                print ("*", end="")
            print("",cont)


        for l in range(cont,1):
            print (" ", end="")
        for m in range(n,0):
            print ("*", end="")
        n-=2
        cont+=1
        print("",cont)
"""
    
 


# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *


# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12


# Una vez resuelto todos los ejercicios, crear un menu de seleccion que permita escoger
# que ejercicio queremos ejecutar hasta que escribamos "salir" ahi recien va a terminar
# de escoger el ejercicio