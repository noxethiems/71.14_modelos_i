from math import sqrt
import random
from utils import guardar_solucion, leer_archivo

class Sucursal:
    def __init__(self, numero,  ubicacion, demanda): 
        self.numero = numero
        self.ubicacion = ubicacion
        self.demanda = demanda

class Camion:
    def __init__(self, ubicacion, capacidad_max):
        self.ubicacion = ubicacion 
        self.capacidad_max = capacidad_max
        self.capacidad = 0

def calcular_recorrido(sucursales, camion, primera_sucursal, menor_recorrido):
    sucursales_visitadas = []
    recorrido = 0

    while(sucursales):
        candidatos = calcular_candidatos(camion, sucursales)

        if len(candidatos) == 0:
            break

        sucursal, distancia = calcular_mas_cercano(camion, candidatos)

        camion.ubicacion = sucursal.ubicacion
        camion.capacidad += sucursal.demanda

        sucursales.remove(sucursal)
        sucursales_visitadas.append(sucursal.numero)
        recorrido += distancia

        if recorrido > menor_recorrido:
            return None, None

    sucursal, distancia = calcular_mas_cercano(camion, [primera_sucursal])
    recorrido += distancia

    print(f"Recorrido: {round(recorrido)}")

    return sucursales_visitadas, recorrido

def calcular_mas_cercano(camion, candidatos):
    if len(candidatos) == 0:
        return None, None
    
    sucursal_cercana = candidatos[0]
    distancia = calcular_distancia(camion, sucursal_cercana)

    for candidato in candidatos:
        nueva_distancia = calcular_distancia(camion, candidato)

        if nueva_distancia < distancia:
            sucursal_cercana = candidato
            distancia = nueva_distancia

    return sucursal_cercana, sqrt(distancia)

# def calcular_mas_cercano(camion, candidatos):
#     if len(candidatos) == 0:
#         return None, None
    
#     [camion_x, camion_y]= camion.ubicacion
#     radio = 1

#     while True:

#         for candidato in candidatos:
#             candidato_x, candidato_y = candidato.ubicacion

#             in_range_x = (camion_x - radio) <= candidato_x <= (camion_x + radio)
#             in_range_y = (camion_y - radio) <= candidato_y <= (camion_y + radio)

#             if in_range_x and in_range_y:
#                 distancia = calcular_distancia(camion, candidato)

#                 return candidato, sqrt(distancia)
            
#         radio*=2

def calcular_candidatos(camion, sucursales):
    candidatos = []

    for sucursal in sucursales:
        posible_capacidad = camion.capacidad + sucursal.demanda
         
        if 0 <= posible_capacidad <= camion.capacidad_max:
            candidatos.append(sucursal)
        
    return candidatos
    
def calcular_distancia(camion, sucursal):
    c_pos = camion.ubicacion
    s_pos = sucursal.ubicacion

    x = (c_pos[0] - s_pos[0]) ** 2
    y = (c_pos[1] - s_pos[1]) ** 2

    return (x + y)

def main():
    file = open("../segundo_problema.txt", "r")
    res = leer_archivo(file)

    demandas = res[0]
    coordenadas = res[1]
    capacidad = res[2]
    dimension = res[3]

    sucursales = []
    sucursales_visitadas = []

    for i in range(dimension):
        sucursal = Sucursal(i + 1, coordenadas[i], demandas[i])
        sucursales.append(sucursal)
    
    menor_recorrido = 100_000_000
    menor_camino= []

    # random.shuffle(sucursales)

    for sucursal in sucursales:

        primera_sucursal = sucursal

        camion = Camion(sucursal.ubicacion, capacidad)
        sucursales_visitadas, recorrido = calcular_recorrido(sucursales.copy(), camion, primera_sucursal, menor_recorrido)

        if sucursales_visitadas == None:
            continue  

        if len(sucursales_visitadas) == dimension:

            if recorrido < menor_recorrido:
                menor_recorrido = recorrido
                menor_camino = sucursales_visitadas

                guardar_solucion(sucursales_visitadas, recorrido)
            
    print("Mejor solución encontrada")
    print(f"Distancia recorrida: {menor_recorrido}!")
    print(f"Camino: {menor_camino}")

if __name__=="__main__":
    main()