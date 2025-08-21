temp = float(input("Ingrese la temperatura:"))
entrada = input("Ingresa la escala de origen, (C, K, F): ")
destino = input("Ingresa la escala de destino, (C, K, F): ")

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
    resultado = ((temp - 32)/1.8) + 32
    print("Su temperatura de grados Fahrenheit a Kelvin, es: ", resultado)
elif entrada == destino:
    print("Igual temperatura")
else:
    print("Error")

