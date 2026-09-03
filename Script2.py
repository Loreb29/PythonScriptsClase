import re


def validar_contrasena(password):
    puntuacion = 0
    problemas = []

    # Longitud
    if len(password) >= 8:
        puntuacion += 1
    else:
        problemas.append("Debe tener al menos 8 caracteres.")

    if len(password) >= 12:
        puntuacion += 1

    # Mayúsculas
    if re.search(r"[A-Z]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos una letra mayúscula.")

    # Minúsculas
    if re.search(r"[a-z]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos una letra minúscula.")

    # Números
    if re.search(r"[0-9]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos un número.")

    # Caracteres especiales
    if re.search(r"[^A-Za-z0-9]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos un carácter especial.")

    # Resultado
    if puntuacion <= 2:
        nivel = "MUY DÉBIL"
    elif puntuacion == 3:
        nivel = "DÉBIL"
    elif puntuacion == 4:
        nivel = "MEDIA"
    elif puntuacion == 5:
        nivel = "FUERTE"
    else:
        nivel = "MUY FUERTE"

    return nivel, puntuacion, problemas


password = input("Introduce una contraseña: ")

nivel, puntuacion, problemas = validar_contrasena(password)

print("\nResultado:")
print(f"Nivel: {nivel}")
print(f"Puntuación: {puntuacion}/6")

if problemas:
    print("\nProblemas:")
    for problema in problemas:
        print(f"- {problema}")
else:
    print("La contraseña cumple todos los requisitos.")import re


def validar_contrasena(password):
    puntuacion = 0
    problemas = []

    # Longitud
    if len(password) >= 8:
        puntuacion += 1
    else:
        problemas.append("Debe tener al menos 8 caracteres.")

    if len(password) >= 12:
        puntuacion += 1

    # Mayúsculas
    if re.search(r"[A-Z]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos una letra mayúscula.")

    # Minúsculas
    if re.search(r"[a-z]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos una letra minúscula.")

    # Números
    if re.search(r"[0-9]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos un número.")

    # Caracteres especiales
    if re.search(r"[^A-Za-z0-9]", password):
        puntuacion += 1
    else:
        problemas.append("Debe contener al menos un carácter especial.")

    # Resultado
    if puntuacion <= 2:
        nivel = "MUY DÉBIL"
    elif puntuacion == 3:
        nivel = "DÉBIL"
    elif puntuacion == 4:
        nivel = "MEDIA"
    elif puntuacion == 5:
        nivel = "FUERTE"
    else:
        nivel = "MUY FUERTE"

    return nivel, puntuacion, problemas


password = input("Introduce una contraseña: ")

nivel, puntuacion, problemas = validar_contrasena(password)

print("\nResultado:")
print(f"Nivel: {nivel}")
print(f"Puntuación: {puntuacion}/6")

if problemas:
    print("\nProblemas:")
    for problema in problemas:
        print(f"- {problema}")
else:
    print("La contraseña cumple todos los requisitos.")