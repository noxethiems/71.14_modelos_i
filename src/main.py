from math import sqrt
import random
from file_utils import leer_archivo

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

def calcular_recorrido(sucursales, camion):
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

    return sucursal_cercana, distancia

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

    return sqrt(x + y)

def main():
    file = open("../primer_problema.txt", "r")

    sucursales = []
    sucursales_visitadas = []
    
    numeros, demandas, coordenadas = leer_archivo(file)

    for i in range(150):
        sucursal = Sucursal(numeros[i], coordenadas[i], demandas[i])
        sucursales.append(sucursal)
    
    menor_recorrido = 1_000_000
    menor_camino= []
    
    for sucursal in sucursales:

        camion = Camion(sucursal.ubicacion, 30)
        sucursales_visitadas, recorrido = calcular_recorrido(sucursales.copy(), camion)  

        if len(sucursales_visitadas) == 150:
            if recorrido < menor_recorrido:
                menor_recorrido = recorrido
                menor_camino = sucursales_visitadas
            
    print("Mejor solución encontrada")
    print(f"Distancia recorrida: {menor_recorrido}!")
    print(f"Camino: {menor_camino}")

if __name__=="__main__":
    main()