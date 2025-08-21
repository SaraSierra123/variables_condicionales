# Se declara la variable precio, para que el usuario lo ingrese
precio = float(input("Ingrese el precio del producto: "))

# Bloque de condiciones que evalua el precio y segun este, se le aplica el respectivo descuento

if precio > 100000:
    descuento = 0.15
    resultado = precio - (precio * descuento)
    print("Su precio con 15% de descuento es:", resultado)
elif precio >= 50000 and precio <= 100000:
    descuento = 0.10
    resultado = precio - (precio * descuento)
    print("Su precio con 10% de descuento es:", resultado)
elif precio >= 10000 and precio <= 49999:
    descuento = 0.05
    resultado = precio - (precio * descuento)
    print("Su precio con 5% de descuento es:", resultado)
else:
    descuento = 0
    resultado = precio
    print("No tienes descuentos, tu precio es:", resultado)

# Preguntar si tiene tarjeta de fidelidad
tarjeta = input("¿Tienes tarjeta de fidelidad? (si/no): ")

if tarjeta == "si":
    resultado = resultado * 0.95  # Se le aplica 5% adicional
    print("Su precio final con tarjeta de fidelidad es:", resultado)
elif tarjeta == "no":
    print("Su precio final es:", resultado)
else:
    print("Dato no válido")