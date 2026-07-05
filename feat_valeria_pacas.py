import random


culturas = [
    "vikinga",
    "inglesa",
    "mongola",
    "bizantina"

]

cultura =random.choice(culturas)
cultura = random.choice(culturas)


evento = input(f"escribe un evento importante de la cultura {cultura}:")


print("información registrada")
print("cultura:", cultura)
print("evento importante:", evento)