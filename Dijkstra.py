def dijkstra(G, s):
  n = len(G)
  visitado = [False]*n
  camino = [None]*n
  costo = [math.inf]*n
  costo[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hq.heappop(queue)
    if not visitado[u]:
      visitado[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < costo[v]:
          costo[v] = f
          camino[v] = u
          hq.heappush(queue, (f, v))

  return camino, costo
