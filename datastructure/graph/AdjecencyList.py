class AdjacencyList:
    def __init__(self):
        self.graph = {}


    def add_vertex(self,vertex):
        graph = self.graph
        graph[vertex] = []


    def delete_vertex(self,vertex):

        graph = self.graph
        if vertex not in graph:
            return

        list = graph[vertex]
        del graph[vertex]
        for x in list:
            if graph[x].__contains__(vertex):
                graph[x].remove(vertex)

    def add_edge(self,source,dest):
        graph = self.graph
        graph[source].append(dest)

    def remove_edge(self,source,dest):
        graph = self.graph
        if source in graph:
            graph[source].remove(dest)


    def has_edge(self,source,dest):
        graph = self.graph
        if source in graph:
            return graph[source].__contains__(dest)
        return False

    def vertex_degree(self,vertex):
        graph = self.graph
        if vertex in graph:
            return len(graph[vertex])
        return False
    def printGraph(self):
        graph = self.graph
        for vertex, list in graph.items():
            print(f"{vertex} : ",end =' ')
            for x in list:
                print(x,end=' ')
            print()


    def depth_first_search(self,vertex, visited = {}):
        graph = self.graph
        if visited is None:
            visited[vertex] = True


if __name__ == "__main__":
    graph = AdjacencyList()
    graph.add_vertex(10)
    graph.add_vertex(20)
    graph.add_vertex(30)
    graph.add_vertex(40)

    graph.add_edge(10,20)
    graph.add_edge(10,40)
    graph.add_edge(10,30)
    graph.add_edge(20,10)
    graph.add_edge(20,30)
    graph.add_edge(20,40)
    graph.add_edge(30,40)
    graph.add_edge(30,10)
    graph.add_edge(40,30)

    graph.printGraph()
    print("==================")
    graph.delete_vertex(60)
    graph.remove_edge(10,30)
    graph.printGraph()
    print(graph.has_edge(40,50))
    print(graph.vertex_degree(60))
    graph.depth_first_search()