from math import sqrt

def main():

    file = open("../primer_problema.txt", "r")
    numeros, demandas, coordenadas = leer_archivo(file)

    sucursales_visitadas = []
    recorrido = 0
    
    sucursales = []

    for i in range(150):
        sucursal = Sucursal(numeros[i], coordenadas[i], demandas[i])
        sucursales.append(sucursal)

    for coordenada in coordenadas:
        print(f"Intentando con {coordenada}...")
        camion = Camion(coordenada, 30)

        aux_sucursales = sucursales.copy()

        sucursales_visitadas, recorrido = intentar_ahre(aux_sucursales, camion)  

        if len(sucursales_visitadas) == 150:
            print(f"Solución encontrada: {recorrido}!")
            print(f"Sucursales visitadas {len(sucursales_visitadas)} y recorrido {recorrido}!")

def intentar_ahre(sucursales, camion):
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
        sucursales_visitadas.append(sucursal)
        recorrido += distancia

    return sucursales_visitadas, recorrido

def leer_archivo(file):
    numeros = []
    demandas = []
    coordenadas = []

    line = siguiente_linea(file)

    while(line != ""):
     
        if line == "DEMANDAS":
            line = siguiente_linea(file)

            while(line != "FIN DEMANDAS"):

                splitted_line = line.split()
                demanda = int(splitted_line[1])

                demandas.append(demanda)

                line = siguiente_linea(file)

        if line == "NODE_COORD_SECTION":
            line = siguiente_linea(file)

            while(line != "EOF"):

                splitted_line = line.split()
                
                coordenada = [
                    float(splitted_line[1]),
                    float(splitted_line[2]),
                ]

                numeros.append(int(splitted_line[0]))
                coordenadas.append(coordenada)

                line = siguiente_linea(file)

        line = siguiente_linea(file)
    
    file.close()

    return numeros, demandas, coordenadas

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
    

def siguiente_linea(file):
    return file.readline().strip()

class Sucursal:
    def __init__(self, numero,  ubicacion, demanda): 
        self.numero = numero
        self.ubicacion = ubicacion
        self.demanda = demanda

class Camion:
    def __init__(self, ubicacion, capacidad):
        self.ubicacion = ubicacion 
        self.capacidad = capacidad

def calcular_distancia(camion, sucursal):
    c_pos = camion.ubicacion
    s_pos = sucursal.ubicacion

    x = (c_pos[0] - s_pos[0]) ** 2
    y = (c_pos[1] - s_pos[1]) ** 2

    return sqrt(x + y)


if __name__=="__main__":
    main()