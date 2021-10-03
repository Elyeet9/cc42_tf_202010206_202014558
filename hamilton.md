# Algoritmo Ciclo Hamiltoniano

Una posible solucion al problema de enrutamiento de vehiculos es el de hallar Ciclos Hamiltonianos.

Un Ciclo Hamiltoniano es un camino en un Grafo el cual pasa por un conjunto de puntos designados (almacen inicial y puntos de entrega en nuestro caso) y regresa al principio. El algoritmo desarrollado para hallar esto es el siguiente:

```
def Hamilton(matriz):
  visitados = []
  n = len(matriz)
  resultados = []
  recorrido = []
  for i in range(n):
    visitados.append(-1)
  visitados[0] = 0
  
  def Siguiente(k):
    while True:
      visitados[k] += 1
      if visitados[k] == n:
        visitados[k] = -1
      if visitados[k] == -1:
        return
      if matriz[visitados[k-1]][visitados[k]] != 0:
        j = 0
        for i in range(k):
          j += 1
          if visitados[i] == visitados[k]:
            break
        if j == k:
          if k < n or k == n:
            return

  def Hamiltoniano(k):
    while True:
      Siguiente(k)
      if visitados[k] == -1:
        return
      
      if k == n - 1:
        aux = []
        for i in range(n):
          aux.append(visitados[i])
        aux.append(0)
        recorrido.append(aux)
        suma = 0
        for i in range(1,n):
          suma += matriz[visitados[i-1]][visitados[i]]
        suma += matriz[visitados[k]][0]
        resultados.append(suma)
      else:
        Hamiltoniano(k+1)

  Hamiltoniano(1)
  aux = resultados[0]
  id_menor = 0
  for i in range(1, len(resultados)):
    if resultados[i] <  aux:
      aux = resultados[i]
      id_menor = i
  
  return resultados[id_menor], recorrido[id_menor]
  ```

Este algoritmo recorre todos los posibles caminos en este grupo de puntos, usando recursividad. Por lo tanto, podemos decir con seguridad que la complejidad algoritmica del algoritmo es de O(n) = n^n