import random

print("bienvenido al juego de adivinar el numero")

while True:
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("\nEstoy pensando en un número del 1 al 10...")

    while True:
        intento = int(input("Escribe tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo")
        elif intento > numero_secreto:
            print("Muy alto")
        else:
            print("Correcto")
            print(f"Lo lograste en {intentos} intentos")
            break

    jugar = input("¿Quieres jugar otra vez? (1-si/ 2-no): ")
    if jugar != "1":
        print("Gracias por jugar")
        break