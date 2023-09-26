def siguiente_linea(file):
    return file.readline().strip()

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