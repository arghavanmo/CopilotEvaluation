

class dag:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        # create a stack
        stack = []
        # create a visited array
        visited = [False] * self.vertices
        # create a list to store the topological sort
        topological_sort = []
        # iterate through the vertices
        for i in range(self.vertices):
            # if the vertex is not visited
            if not visited[i]:
                # call the recursive function
                self.topological_sort_util(i, visited, stack, topological_sort)
        # reverse the list
        topological_sort.reverse()
        # return the topological sort
        return topological_sort

    def topological_sort_util(self, i, visited, stack, topological_sort):
        # mark the vertex as visited
        visited[i] = True
        # iterate through the adjacency list
        for j in self.graph[i]:
            # if the vertex is not visited
            if not visited[j]:
                # call the recursive function
                self.topological_sort_util(j, visited, stack, topological_sort)
        # push the vertex to the stack
        stack.append(i)

