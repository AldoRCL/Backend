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