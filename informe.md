# Informe de WASC de Participación
### Complejidad Algorítmica

### Alumnos
- Flores Tenorio, Juan Diego Enrique
- Goyas Ayllón, Leonardo Andre

### Profesor
- Canaval Sanchez, Luis Martin

### Ciclo
2021-02

## Introducción
El problema de enrutamiento de vehículos, conocido a partir de la definición de Dantzig y Ramser (1959), es una generalización del Problema del Agente Viajero, que involucra la optimización y programación para hallar el coste mínimo total entre las rutas disponibles en un grafo.

El presente trabajo tiene como finalidad resolver el problema de enrutamiento de vehículos a través de la implementación de algoritmos complejos de búsqueda en grafos y hallazgo del camino menor en un grafo con pesos.
Los softwares empleados son Google Colab, en el cual se gestionó el apartado relacionado al código fuente, y GitHub, donde se organizó mediante issues la responsabilidad de las diversas entregas a lo largo del ciclo. Se utilizó el lenguaje Python y las diversas librerías disponibles en este.

## Objetivos
### Objetivo General
- Identificar, analizar y resolver el problema de enrutamiento de vehículos aplicando el razonamiento cuantitativo.
### Objetivos Específicos
- Aplicar los conocimientos adquiridos en el curso Complejidad Algorítmica para diseñar una solución óptima en el lenguaje Python al problema de enrutamiento de vehículos.
- Implementar un programa que utilice responsablemente los recursos computacionales.
- Emplear los métodos de búsqueda en grafos para encontrar la ruta óptima en un grafo asociado al enrutamiento de vehículos.

## Algoritmos Generales
Se consideran 2 algoritmos generales, que representan la generación aleatoria de los puntos de entrega y almacenaje entre el millón de distintos puntos y la visualización gráfica con estos datos. Dado que no fueron definidos dentro de una función, serán denominados como “Algoritmo 1” para el caso de la generación de puntos y “Algoritmos 2” para el caso de la visualización gráfica.
- El Algoritmo 1 emplea la librería numpy para generar cuatro números aleatorios, los dos primeros simbolizan la cantidad de puntos de almacenaje y entrega que existen en el grafo y los dos siguientes representan el índice de dichos puntos, los cuales son indexados en dos listas separadas por tipo de punto. Estos datos serán de ayuda para distribuir los puntos por su posición en los ejes coordenados y color.
- El Algoritmo 2 emplea la librería matplotlib para la visualización gráfica del grafo con los datos generados en el Algoritmo 1. El tipo de gráfica es un grafo de dispersión, donde los colores negro, rojo y verde representan los “puntos libres”, los puntos de almacenaje y los puntos de entrega respectivamente.

## Algoritmos aplicados
### Leonardo Goyas
- dijkstra: El algoritmo de Dijkstra permite hallar el camino más corto para conectar un grafo y ha sido aplicado de tal manera que retorna dos listas. La primera guarda el nodo de donde viene, es decir, si en la posición 4 nos muestra el nodo 5, significa que el camino hacia 4 viene de 5. En la segunda lista guarda el costo que tiene el camino entre los dos nodos de la anterior lista.
- matriz_reducida: Este algoritmo recibe un grafo (para este caso el grafo completo de nuestro mapa), las posiciones de un nodo inicial y uno final. Calculando los mínimos y máximos, usamos ecuaciones para crear un nuevo grafo conteniendo solamente los nodos que estén dentro de esta nueva red de nodos. La función retorna el nuevo grafo y la posición local del nuevo nodo inicial y final. Este algoritmo es usado junto al criterio de cercanía para aumentar la eficiencia en ejecución.
- algoritmo_leonardo: Este algoritmo recibe los mismos parámetros que matriz_reducida. Primero creamos un grafo reducido con el algoritmo antes mencionado. Luego, ejecutamos dijkstra en este grafo para obtener el camino más corto con estas coordenadas locales. Recorremos la lista de caminos desde el nodo final y regresamos hasta el nodo inicial, revirtiendo la lista al terminar para tenerla en orden. Finalmente, se pasan estas posiciones por una ecuación que permite traducir sus coordenadas locales a las coordenadas del mapa real.
Para ejecutar este algoritmo, se pide input al usuario para que ingrese las coordenadas de un almacén y todos los puntos de entrega que desee recorrer. Se ordenan los puntos de entrega según el criterio de cercanía y se ejecuta el algoritmo para encontrar el camino más corto por cada punto al siguiente. De este modo, solamente se usará un grafo reducido por cada trayecto, mejorando la eficiencia del proyecto.
### Juan Diego Flores
- x_menos1: La función se encarga de verificar que los parámetros sean retornados como un valor positivo, su utilidad se puede comparar con el valor absoluto.
- Closest_points: La función se encarga de hallar los puntos cercanos al punto de almacén elegido respecto al resto de puntos de almacenaje. Está restringida a una cantidad dada por el usuario mediante los parámetros dado que el algoritmo es Fuerza Bruta (un valor considerablemente alto retrasaría la compilación en varias decenas de minutos).
- weighted_array: La función almacena dentro de una lista las aristas del grafo con su respectivo peso, que en este caso está representado por la distancia entre ambos vértices. Su función se equipara a la creación de la una matriz de pesos, que posteriormente sería utilizada en 
- Hamilton: El algoritmo principal para la búsqueda del camino más corto desde el punto de almacenaje a los puntos de entrega. Aplica la Fuerza Bruta para encontrar todos los posibles caminos y posteriormente los evalúa para encontrar el que tenga como resultado el menor valor.

## Conclusiones
- Se consiguió identificar, analizar y resolver el problema de enrutamiento de vehículos aplicando el razonamiento cuantitativo en el desarrollo de soluciones codificadas.
- La solución al problema de enrutamiento de vehículos es factible de aplicar mediante algoritmos computacionales complejos debido a la simplicidad de su aplicación. 
- Se consiguió implementar un código que utilice responsablemente los recursos computacionales, teniendo como tiempo aproximado de compilación los 4 minutos.
- Los métodos de búsqueda en grafos fueron imprescindibles para la búsqueda de la ruta óptima, siendo el menos exigente el algoritmo diseñado por Leonardo Goyas Ayllón.
- La aplicación del método práctico-teórico llevada a cabo por los integrantes del equipo de trabajo fue óptima para alcanzar las competencias planteadas para el Trabajo Final del curso Complejidad Algorítmica.

## Recomendaciones
- Los alumnos encontraron que la escritura y posterior lectura de los datos en archivos para la aplicación de los mismos tiene un tiempo de compilación notoriamente menor a la indexación en listas o tuplas.
- El algoritmo de Fuerza Bruta puede ser reemplazado por uno de menor tiempo asintótico, dado que este tiene como notación n! (factorial de n) y resulta extremadamente ineficiente en cantidades mayores de vértices.
- Se recomienda emplear el método práctico-teórico para tener un resultado óptimo en proyectos similares.
