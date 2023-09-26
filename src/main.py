from math import sqrt
from file_utils import leer_archivo

class Sucursal:
    def __init__(self, numero,  ubicacion, demanda): 
        self.numero = numero
        self.ubicacion = ubicacion
        self.demanda = demanda

class Camion:
    def __init__(self, ubicacion, capacidad):
        self.ubicacion = ubicacion 
        self.capacidad = capacidad

def calcular_recorrido(sucursales, camion):
    sucursales_visitadas = []
    recorrido = 0

    while(sucursales):
        cantidatos = calcular_candidatos(camion, sucursales)
        sucursal, distancia = calcular_mas_cercano(camion, cantidatos)

        if sucursal == None:
            break

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
         
        if 0 <= posible_capacidad <= 30:
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
    numeros, demandas, coordenadas = leer_archivo(file)

    sucursales = []
    sucursales_visitadas = []
    recorrido = 0

    for i in range(150):
        sucursal = Sucursal(numeros[i], coordenadas[i], demandas[i])
        sucursales.append(sucursal)

    for coordenada in coordenadas:
        camion = Camion(coordenada, 30)

        aux_sucursales = sucursales.copy()
        sucursales_visitadas, recorrido = calcular_recorrido(sucursales.copy(), camion)  

        if len(sucursales_visitadas) == 150:
            print(f"Solución encontrada!")
            print(f"Sucursales visitadas {len(sucursales_visitadas)} y recorrido {recorrido}!")
            print(sucursales_visitadas)

if __name__=="__main__":
    main()