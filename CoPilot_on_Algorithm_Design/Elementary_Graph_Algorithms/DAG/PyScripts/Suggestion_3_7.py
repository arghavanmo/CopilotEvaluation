

# Compare this snippet from algorithm_design/elementry graph algorithms/dag.py:
# # implement a graph structure.
# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [None] * self.V
#         for i in range(self.V):
#             self.graph[i] = []
# 
#     def add_edge(self, u, v):
#         self.graph[u].append(v)
# 
#     def is_connected(self, u, v):
#         return True if v in self.graph[u] else False
# 
#     def print_graph(self):
#         for i in range(self.V):
#             print(i, ""-->"", self.graph[i])
# 
#     # given a source vertex, return the list of all vertexes that can be reached from the source vertex.
#     # ! faulty code
#     def dfs(self, s):
#         visited = [False] * self.V
#         self.dfs_util(s, visited)
# 
#     def dfs_util(self, s, visited):
#         visited[s] = True
#         print(s, end="" "")
#         for i in self.graph[s]:
#             if visited[i] == False:
#                 self.dfs_util(i, visited)
# 
#     # given a source vertex, return the list of all vertexes that can be reached from the source vertex in a depth-first manner.
#     # ! faulty code
#     def dfs_path(self, s, d):
#         visited = [False] * self.V
#         stack = []
#         stack.append(s)
#         visited[s] = True
#         path = []
#         while stack:
#             s = stack.pop()
#             path.append(s)
#             if s == d:
#                 return path
#             for i in self.graph[s]:
#                 if visited[i] == False

