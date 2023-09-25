from math import sqrt

def main():

    file = open("../primer_problema.txt", "r")
    line = siguiente_linea(file)

    demandas = []
    coordenadas = []

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

                coordenadas.append(coordenada)

                line = siguiente_linea(file)

        line = siguiente_linea(file)
    
    file.close()

    sucursales = []
    camion = Camion([0,0], 30)
    
    largo = len(coordenadas)

    for i in range(largo):
        sucursal = Sucursal(coordenadas[i], demandas[i])
        sucursales.append(sucursal)

    recorrido = 0

    while(len(sucursales) > 0):
        cantidatos = calcular_candidatos(camion, sucursales)
        sucursal, distancia = calcular_mas_cercano(camion, cantidatos)
        
        camion.ubicacion = sucursal.ubicacion
        camion.capacidad += sucursal.demanda

        sucursales.remove(sucursal)
        recorrido += distancia

    print(recorrido)


def calcular_mas_cercano(camion, candidatos):
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
            print("posible")
            candidatos.append(sucursal)
        
    return candidatos
    

def siguiente_linea(file):
    return file.readline().strip()

class Sucursal:
    def __init__(self, ubicacion, demanda): 
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