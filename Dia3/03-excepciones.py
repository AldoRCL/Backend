
"""
try:
    numero = input("Ingresa un numero")
    print(int(numero)+10)
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Debiste ingresar un numero!!!")
except :
    print("Algo salio Mal")
print("Yo soy el codigo restante")

# finally => no le importa si todo salio bion o si hubo un error, igual se ejecutara, Pero luego mostrara el si esque no se declaro un except
try:
    print(10/1)
except:
    print("error")
else:
    print("TODO BIEN")
finally:
    print("Yo me ejecuto si o si")
"""
number = []
for i in range(1,5):

    try:
        ingreso = int(input(f"Ingresa un numero {i}: "))
        number.append(ingreso)
    except:
        print("Numero Incorrecto")
print("Los numeros ingresados son: ",number)
    
