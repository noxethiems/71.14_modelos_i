def siguiente_linea(file):
    return file.readline().strip()

def leer_archivo(file):
    
    demandas = []
    coordenadas = []

    capacidad = 0
    dimension = 0

    line = siguiente_linea(file)

    while(line != ""):

        if "CAPACIDAD" in line:
            splitted_line = line.split()
            capacidad = int(splitted_line[1])

        elif "DIMENSION" in line:
            splitted_line = line.split()
            dimension = int(splitted_line[1])

        elif line == "DEMANDAS":
            line = siguiente_linea(file)

            while(line != "FIN DEMANDAS"):

                splitted_line = line.split()
                demanda = int(splitted_line[1])

                demandas.append(demanda)

                line = siguiente_linea(file)

        elif line == "NODE_COORD_SECTION":
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

    return demandas, coordenadas, capacidad, dimension

def guardar_solucion(sucursales_visitadas, recorrido):
    file = open("../solución_2.txt", "w")
    file.write(f"Distancia: {round(recorrido)}\n")
    file.write(f"{sucursales_visitadas}\n")