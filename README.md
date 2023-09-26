# 71.14_modelos_i

# Enunciado
Un camión de caudales debe entregar y recibir dinero de diferentes sucursales bancarias.
Sale de la central vacío y en ningún momento la carga puede superar un importe definido (tampoco ser negativa).
Se busca encontrar el recorrido más corto pasando por todas las sucursales.
Formato del archivo del problema
Cada línea comienza con una palabra que indica el tipo de información

CAPACIDAD: CCC
Importe máximo a transportar
DIMENSION: NNN
NNN cantidad de sucursales
DEMANDAS
Seguido de NNN (cantidad de sucursales) renglones con la forma
N D
donde N es el número de sucursal y D su demanda (con signo '-' en caso de entregar dinero)
Finaliza con una lí "FIN DEMANDAS"
- Impresión del problema
Me costó mucho encontrar una mejor solución que esta. No fue largo de codear pero sentí que no tenía el modelo que optimizar mejor.

- Ideas de como lo van a intentar resolver
Lo que hice fue encontrar candidatos posibles y luego elegir el más cercano. Inicié el problema desde distintas sucursales con el camión vacío.

- Comentarios sobre los cambios que hagan en el código a medida que intentan mejorar el resultado. Comentar y explicar los diferentes intentos que van haciendo, incluir pros y contras esperados/encontrados
Al principio tuve un bug donde iniciaba el camión lleno por error, cuando lo que quería indicar era la capacidad máxima y no la capacidad en el momento dado.

- Comentarios finales de la entrega
Una disculpa por la demora, me había confundido la fecha de la entrega, erróneamente creí que era la semana que viene.