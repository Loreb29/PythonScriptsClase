from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def crear_clave():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    print("Clave creada y guardada en:", KEY_FILE)


def cargar_clave():
    if not os.path.exists(KEY_FILE):
        print("No existe una clave. Creando una nueva...")
        crear_clave()

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encriptar():
    key = cargar_clave()
    fernet = Fernet(key)

    texto = input("Texto a encriptar: ")

    encrypted = fernet.encrypt(texto.encode())

    print("\nTexto encriptado:")
    print(encrypted.decode())


def desencriptar():
    key = cargar_clave()
    fernet = Fernet(key)

    texto = input("Texto encriptado: ")

    try:
        decrypted = fernet.decrypt(texto.encode())

        print("\nTexto desencriptado:")
        print(decrypted.decode())

    except Exception:
        print("La clave o el texto encriptado no son válidos.")


def main():
    while True:
        print("\n--- FERNET ---")
        print("1. Crear nueva clave")
        print("2. Encriptar")
        print("3. Desencriptar")
        print("4. Salir")

        opcion = input("\nOpción: ")

        if opcion == "1":
            crear_clave()

        elif opcion == "2":
            encriptar()

        elif opcion == "3":
            desencriptar()

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()