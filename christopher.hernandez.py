import random

numero = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número: "))

    if intento == numero:
        print("¡you won!")
        break
    elif intento < numero:
        print("the number is higher")
    else:
        print("the number is lower")
        


        