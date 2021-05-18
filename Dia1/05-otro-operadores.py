# Operadores de Comparacion
# == es igual que | en python no hay el triple doble igual
# != diferente que 
# <, >, menor que ,mayor que 
# <=, >=, menor o igual que , mayor igual que

numero1, numero2 =10,20
print(numero1 < numero2)

print((10 > 5) and (10 > 11))# Solo 1 tiene que ser falso para que todo sea falso
print((10 >= 10) or (10 > 20))# Solo 1 tiene que ser verdadero para que todo sea verdadero
print(not(10 >= 10) or (10 >20) )

# Operadores de identidad
# is => es
# is not => no es
# sirve para ver si estan apuntando a la misma direccion de memoria
frutas = ['MANZANA','PIÑA','FRESA','SANDIA']
frutas2 = frutas
print(frutas is frutas2)
# dos tipos de variables => variables MUTABLES y las variables INMUTABLES
# mutables => es cuando nostros hacemos una copia de esa variable,la copia tambien se esta alojando en el mismo espacio de memoria
# inmutables => es cuando hacemos una copia esta copia se alojara en otra posicion de memoria

nombres =['eduardo','raul','carlos','estefani']
nombres_alumnos = nombres
nombres_alumnos[0] = ['carmen']
nacionalidad = "ecuatoriana"
nacionalidad2 = nacionalidad
nacionalidad2 = "brazileña"
print(nombres)
print(nacionalidad)
print(nacionalidad is nacionalidad2)
print(nombres is nombres_alumnos)
# Sirve para ubicar el identificar el nico de esa variable  para saber la posicion en la cual se encuentra esa variabletendriamos que convertir a hexadecimal ese valor
print(id(nombres))
print(hex(id(nombres)))