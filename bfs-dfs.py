def Graph():
  graph = {}
  arr = input("enter vetices:").split()
  for el in arr:
    graph[el] = []
  while(1):
    arr2 = input("enter edge (to quit enter q):").split()
    if arr2[0] != "q":
      if not(arr2[1] in graph[arr2[0]]):
        graph[arr2[0]].append(arr2[1])
    else:
      break
  return graph

visited = set()

# DFS
def dfs(visited, graph, node, elem):
  if node == elem:
    print(node)
    return True
  elif node not in visited:
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
      result = dfs(visited, graph, neighbour, elem)
      if result:
        return True
  return False

visited = set()
queue = []

# BFS
def bfs(visited, graph, node, elem):
  queue.append(node)
  while len(queue) != 0:
    n_node = queue.pop(0)
    visited.add(n_node)
    print(n_node)
    if n_node == elem:
      return True 
    for neighbour in graph[n_node]:
      if not(neighbour in visited):
        queue.append(neighbour)
  return False

if __name__ == "__main__":
    graph = Graph()
    sn = input("Enter source node :")
    gn = input("Enter goal node :")
    algo = int(input("1. DFS \n2. BFS \nEnter your choice : "))
    if algo == 1:
        print("Path between node {} and node {} exist : {}".format(sn, gn, dfs(visited, graph, sn, gn)))
    elif algo == 2:
        print("Path between node {} and node {} exist : {}".format(sn, gn, bfs(visited, graph, sn, gn)))
    else:
        print("Invalid choice!!")