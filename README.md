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
EDGE_WEIGHT_TYPE : XXX
EUC_2D
Luego un renglón NODE_COORD_SECTION
Seguido de NNN (cantidad de sucursales) renglones con la forma
N X Y
donde N es el número de sucursal y X,Y su ubicación
Finaliza con un renglón "EOF"
La distancia entre las sucursales i y j es sqrt((Xi-Xj)^2+(Yi-Yj)^2)
Formato del archivo de la solución
Sucursales según orden de visita separando por espacio
Ej: 11 32 22 1 33 ...
Entregas
El force push sobre el repo github implica la desaprobación de todo el TP

Subir la mejor solución posible

En el repo github creen un archivo "entrega_N.txt" (N: nombre del problema), CADA ENTREGA debe contener

- Impresión del problema. Les parece fácil, difícil, largo, corto, cambios en relación a la entrega anterior, lo asocian a otro problema, comentarios, etc.
- Ideas de como lo van a intentar resolver
- Comentarios sobre los cambios que hagan en el código a medida que intentan mejorar el resultado. Comentar y explicar los diferentes intentos que van haciendo, incluir pros y contras esperados/encontrados
- Comentarios finales de la entrega
    