import random

print("** Generador de contraseñas ***")
print("*******")

# Validamos que el usuario ingrese un número correcto
tam = 0
while tam <= 0:
    try:
        tam = int(input("¿Cuántos caracteres tendrá la contraseña? "))
    except:
        print("Debes ingresar un número válido.")

# Preguntamos si quiere generar más de una contraseña
cantidad = 1
try:
    cantidad = int(input("¿Cuántas contraseñas deseas generar? (mínimo 1): "))
    if cantidad < 1:
        cantidad = 1
except:
    cantidad = 1

# Caracteres permitidos
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-+,.;:?"

print("\nGenerando contraseña(s)...\n")

# Usamos un for para generar varias contraseñas sin cambiar la lógica original
for j in range(cantidad):

    contrasena = ""  # contraseña vacía por cada ciclo

    # Generamos carácter por carácter (tu misma esencia)
    for i in range(tam):
        numero = random.randint(0, len(caracteres) - 1)
        contrasena = contrasena + caracteres[numero]

    print(f"Contraseña #{j+1}: {contrasena}")

print("\nGuárdala(s) en un lugar seguro.")