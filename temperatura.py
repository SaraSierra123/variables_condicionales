# Declaramos las variables de entrada y destino, para que el usuario ingrese deseada, ademas de la variable para que ingrese la temperatura

temp = float(input("Ingrese la temperatura:"))
entrada = input("Ingresa la escala de origen, (C, K, F): ")
destino = input("Ingresa la escala de destino, (C, K, F): ")

# Bloque de condicionales que realizan la conversion de temperatura, segun las unidades de entrada y las de destino

if entrada == "C" and destino == "K":
    resultado = temp + 273.15
    print("Su temperatura de grados Celcius a Kelvin, es: ", resultado)
elif entrada == "C" and destino == "F":
    resultado = (1.8 * temp) + 32
    print("Su temperatura de grados Celcius a Fahrenheit, es: ", resultado)
elif entrada == "K" and destino == "C":
    resultado = temp - 273.15
elif entrada == "K" and destino == "F":
    resultado = ((temp - 273.15)*1.8) +32
    print("Su temperatura de grados kelvin a Fahrenheit, es: ", resultado)
elif entrada == "F" and destino == "C":
    resultado = (temp-32)/1.8
    print("Su temperatura de grados Fahrenheit a Celcius, es: ", resultado)
elif entrada == "F" and destino == "K":
    resultado = ((temp - 32)/1.8) + 273.15
    print("Su temperatura de grados Fahrenheit a Kelvin, es: ", resultado)
elif entrada == destino:
    print("Igual temperatura")

# Si no se cumple con ninguna condicion se muetsra un error
else:
    print("Error")

