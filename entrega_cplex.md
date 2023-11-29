### 71.14 MODELOS Y OPTIMIZACIÓN I (Curso Oitana)

### Problema del viajero
Número de ciudades = 100
Capacidad = sin límite de capacidad

## MTZ (Miller-Tucker-Zemlin)
Evitar subtours añadiendo variables para indicar un orden y restricciones para que este orden sea creciente y se visiten todas las ciudades, habiendo entrado y salido una vez de cada una.

Ventajas:
Garantiza que no haya subciclos en la solución óptima.

Desventajas:
Es más costoso computacionalmente.

### Ejecuciones
- Tiempo de ejecución sin solución agregada: 03:34:93
- Valor de la función objetivo (distancia): 5249.622889689
- Tiempo de ejecución sin solución agregada¹: Al momento no pude inicializar la solución

![MTZ sin solución inicial añadida](/imgs/mtz_sin_solucion.jpeg)

## Eliminación de subtours
Obtiene una solución inicial, identifica los subtours y añade nuevas restricciones para eliminarlos, vuelve a ejecutarse y se identifican nuevos subtoures, y así sucesivamente.

Ventajas:
Llega a una solución sin ser tan costoso computacionalmente

Desventajas:
Puede iterar una gran cantidad de veces antes de hallar una solución.


### Ejecuciones
- Tiempo de ejecución sin solución agregada: 00:15:40
- Valor de la función objetivo sin solución agregada: 5249.622889689
- Tiempo de ejecución con solución agregada¹: 00:15:33
- Valor de la función objetivo con solución agregada¹: 5249.847006283 

## Nueva solución de heurística
  - Valor de la función objetivo: 5632 
  - Tiempo de ejecución: aproximadamente 5 minutos

¹ Solución encontrada: 64 44 71 45 4 68 91 13 74 31 27 49 72 80 14 77 15 78 59 16 79 88 94 10 63 48 73 76 87 1 98 34 30 84 7 8 89 96 35 93 52 33 92 54 46 90 56 26 75 18 85 65 55 58 50 70 86 29 81 25 20 51 43 67 32 23 38 41 57 39 60 66 17 11 61 36 69 24 12 53 40 42 9 28 6 37 2 19 99 47 83 97 100 5 95 82 3 62 22 21

## Solución de CPLEX para eliminación de subtours (con solución agregada)
87 81 62 68 95 99 8 89 28 3 61 53 74 77 78 59 11 75 2 51 64 21 49 12 20 97 41 6 86 84 27 38 92 76 93 69 9 23 60 47 57 37 67 71 4 90 42 63 72 58 43 33 40 46 65 26 39 55 79 66 36 22 30 44 85 17 32 91 24 50 45 80 48 31 83 73 15 16 88 14 29 98 56 7 18 70 34 94 96 25 13 54 52 10 82 35 100 1 19 5
