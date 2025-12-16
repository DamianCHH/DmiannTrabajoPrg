import random

print("** Generador de contraseñas ***")
print("*******************************")
print("///////////////////////////////")
# -------------------------------
# Definiendo una funcion para generar una contraseña
# -------------------------------
def generar_contrasena(tamano, caracteres):
    
    contrasena = ""

    for i in range(tamano):
        numero = random.randint(0, len(caracteres) - 1)
        contrasena = contrasena + caracteres[numero]

    return contrasena


# Validamos que el usuario ingrese un número correcto
tam = 0
while tam <= 0:
    try:
        tam = int(input("¿Cuántos caracteres tendrá la contraseña? "))
    except:
        print("Debes ingresar un número válido.")

# Preguntamos cuántas contraseñas desea generar
cantidad = 1
try:
    cantidad = int(input("¿Cuántas contraseñas deseas generar? (mínimo 1): "))
    if cantidad < 1:
        cantidad = 1
except:
    cantidad = 1



# Generamos una Tupla

caracteres = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-+,.;:?")

print("\nGenerando contraseña(s)...\n")

# Generamos las contraseñas usando la función
for j in range(cantidad):
    contrasena = generar_contrasena(tam, caracteres)
    print(f"Contraseña #{j+1}: {contrasena}")

print("\nGuárdala(s) en un lugar seguro.")
