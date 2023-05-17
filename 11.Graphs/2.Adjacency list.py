# Graph Node used for adjacency list
class GraphNode:
    def __init__(self,val) -> None:
        self.val = val
        self.neighbors = []
    
# Or, use a hashmap
adjList = {"A":[],"B":[]}

# Given directed edges, build an adjacency list
edges = [ ["A","B"],["B","C"],["B","E"],["C","E"],["E","D"] ]

adjList = {}

for src,dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

# adjList = {"A":["B"],"B":["C","E"],"C":["E"],"E":["D"]}

# DFS on adjacency list

# Count paths ( backtracking )
def dfs(node,target,adjList,visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor,target,adjList,visit)
    visit.remove(node)
    return count

print(dfs("A","E",adjList,set()))

# TC : O(N^V)
# SC : O(N)

# BFS on adjacency list

# Shortest path from node to target
from collections import deque
def bfs(node,target,adjList):
    length = 0
    visit = set()
    queue = deque()
    visit.add(node)
    queue.append(node)
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
        for neighbor in adjList[node]:
            if neighbor not in visit:
                visit.add(neighbor)
                queue.append(neighbor)
        length += 1
    return length

print(bfs("A","E",adjList))

# TC : O(V+E)
# SC : O(V)

