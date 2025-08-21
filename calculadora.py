'''
Primero vamos a definir las variables que utilizaremos; las dos entradas y la operacion
que desea realizar el usuario
'''
numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
operador = input("Ingresa la operacion deseada: ")

'''
Creamos la condicion de que si coinciden la operacion y el operador, se realiza el
respectivo procedimiento y se imprime el resultado
'''

# Si la operacion ingresada es suma, se suman las dos entradas
if operador == "suma":
    resultado = numero1 + numero2
    print("El resultado es: ", resultado)

# Si la operacion ingresada es resta, se restan las dos entradas
elif operador == "resta":
    resultado = numero1 - numero2
    print("El resultado es: ", resultado)

# Si la operacion ingresada es multiplicacion, se multiplican las dos entradas
elif operador == "multiplicacion":
    resultado = numero1 * numero2
    print("El resultado es: ", resultado)

# Si la operacion ingresada es division, primero se verifica que el divisor no sea 0
elif operador == "division":
    #Si es 0, se muestra un error, sino se dividen las dos entradas
    if numero2 == 0:
        print("Error, resultado no definido")
    else:
        resultado = numero1 / numero2
        print("El resultado es:", resultado)

# Si la operacion igresada no coincide con el operador, se muestra un error
else:
    print("Operacion no valida")
    