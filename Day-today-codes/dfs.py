def dfs(graph, source, visited):
  if(visited[source] == True):
    return
  
  visited[source] = True
  print(source)

  for v in range(len(graph[source])):
    # print(v)
    if(not visited[v] and graph[source][v]):
      dfs(graph, v, visited)

def main():
  # nNodes, nEdges = map(int, input().split())
  # graph = [ [0 for j in range(nNodes)] for i in range(nNodes)]
  # for i in range(nEdges):
  #   u, v = map(int, input().split())
  #   graph[u][v] = 1
  #   graph[v][u] = 1
  graph = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
  visited = [False for i in range(5)]
  dfs(graph,0,visited)

if __name__ == "__main__":
  main()
