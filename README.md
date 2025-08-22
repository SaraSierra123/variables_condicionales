# variables_condicionales

Este repositorio contiene 4 programas en Python que utilizan variables y
estructuras condicionales para resolver distintos problemas.

## programas:

### 1. calculadora.py

**descripcion**\
Una calculadora básica con operaciones de suma, resta,
multiplicación y división.

**ejemplo**

    ingresa numero 1: 4
    ingresa numero 2: 3
    ingresa tipo de operacion: suma, resta, multiplicacion o division
    operacion: multiplicacion
    resultado: 12

**posibles errores** - División entre 0. - Ingresar letras en vez de
números. -Que el usuario ingrese mayusculas o comas en el tipo de operacion.

------------------------------------------------------------------------

### 2. temperatura.py

**descripcion**\
Convierte temperaturas entre Celsius, Fahrenheit y Kelvin.

**ejemplo**
    Ingrese el valor de la temperatura: 40
    Ingresa la escala de origen, (C, K, F): Celsius
    Ingresa la escala de destino, (C, K, F): Kelvin
    Su temperatura de grados Celcius a Kelvin, es: 313.15

**posibles errores** - Ingresar un tipo de escala inválido. - Usar
mayúsculas o minúsculas diferentes.

------------------------------------------------------------------------

### 3. edad_votante.py

**descripcion**\
Determina si una persona puede votar según su país y edad. Incluye
reglas para Argentina, Indonesia, Colombia, Corea del Sur y Singapur.

**ejemplo**

    Ingresa tu país (Colombia, Estados Unidos, Japón, Brasil, Argentina): Colombia
    Ingresa tu edad: 18
    Tienes la edad suficiente para votar en Colombia

**posibles errores** - Ingresar un país que no está en la lista. - Usar
otro formato de nombre (mayúsculas/minúsculas).

------------------------------------------------------------------------

### 4. descuentos_tienda.py

**descripcion**\
Calcula el precio final de un producto aplicando descuentos:

-   100,000 → 15% de descuento

-   50,000 a 100,000 → 10%

-   10,000 a 49,999 → 5%

-   Tarjeta de fidelidad → +5% adicional

**ejemplo**

    Ingrese el precio del producto: 105000
    Su precio con 15% de descuento es: 89250.0
    ¿Tienes tarjeta de fidelidad? (si/no): si
    Su precio final con tarjeta de fidelidad es: 84787.5

**posibles errores** - Escribir el precio con separador de miles
(`105.000` en vez de `105000`). - Ingresar texto en lugar de números.
