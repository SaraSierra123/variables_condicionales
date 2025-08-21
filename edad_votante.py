
# Declaracion de variables
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país (Colombia, Estados Unidos, Japón, Brasil, Argentina): ")

# Verificación de edad con if, elif y else
if pais == "Colombia":
    if edad >= 18:
        print("Tienes la edad suficiente para votar en Colombia")
    else:
        print("Aún no puedes votar en Colombia (Edad minima:18 años)")

elif pais == "Estados Unidos":
    if edad >= 18:
        print("Tienes la edad suficiente para votar en Estados Unidos")
    else:
        print("Aún no puedes votar en Estados unidos (Edad minima:18 años)")

elif pais == "Japón":
    if edad >= 18:
        print("Tienes la edad suficiente para votar en Japon")
    else:
        print("Aún no puedes votar en Japon (Edad minima:18 años)")

elif pais == "Brasil":
    if edad >= 16:
        print("Tienes la edad suficiente para votar en Brasil")
    else:
        print("Aún no puedes votar en Brasil (Edad minima:16 años)")

elif pais == "Argentina":
    if edad >= 16:
        print("Tienes la edad suficiente para votar en Argentina")
    else:
        print("Aún no puedes votar en Argentina (Edad minima:16 años)")

else:
    print("Lo siento, no tengo información sobre la edad para votar en ese país.")
