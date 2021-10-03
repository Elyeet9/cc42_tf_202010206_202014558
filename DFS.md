Análisis de Depth First Search:

El algoritmo Depth First Search, mejor conocido como DFS, se encarga de atravesar o buscar información
en un árbol o grafo. Este algoritmo inicia en el nodo designado arbitrariamente como raíz y explora
tan lejos como sea posible por las ramas del grafo antes de realizar backtracking.

El algoritmo diseñado en Python es el siguiente:

'''
def DFS_(G, s):
  n = len(G)
  visitado=[False]*n
  padre=[None]*n

  def _DFS(i):
    visitado[i] = True
    for j in G[i]:
      if not visitado[j]:
        padre[j]=i
        _DFS(j)
  _DFS(s)
  
  return padre 
'''

Tiene un tiempo asintótico de n log(n) debido al empleo de recursividad. Por tanto, se puede concluir que
su Big O corresponde a (n)