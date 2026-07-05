import time

nivel_bateria = 0
capacidad_maxima = 100
carga = 5

tipo_cargador = input("Ingrese el tipo de cargador (rápido/lento): ").lower()

if tipo_cargador == "rápido":
    carga = 10
elif tipo_cargador == "lento":
    carga = 2

print("Iniciando carga...")

while nivel_bateria < capacidad_maxima:
    nivel_bateria += carga
    
    if nivel_bateria > capacidad_maxima:
        nivel_bateria = capacidad_maxima
        
    print(f"Carga actual: {nivel_bateria}%")
    time.sleep(1)

print("¡Batería cargada al 100%! Desconecte el cargador.")
