graph={}

def add_edge(u,v):
  if u not in graph:
    graph[u]=[]
  if v not in graph:
    graph[v]=[]
  graph[u].append(v)
  graph[v].append(u)

def DFS(node , visited):
  visited.append(node)
  print(node,end=" ")
  for neighbour in graph[node]:
    if neighbour not in visited:
      DFS(neighbour,visited)

def BFS(start):
  visited=[]
  queue=[]
  
  visited.append(start)
  queue.append(start)

  while len(queue)>0:
    print(queue[0],end=" ")
    temp=queue[0]
    queue.pop(0)
    for neighbour in graph[temp]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


n=int(input("enter the number of nodes"))
e=int(input("enter the number of edges"))
print("enter edge")
for i in range(e):
  u=int(input("enter the first node (u)"))
  v=int(input("enter the second node (v)"))
  add_edge(u,v)

start=int(input("enter the start point"))

print("DFS",end=" ")
DFS(start,[])

print("BFS",end=" ")
BFS(start)