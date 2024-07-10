class graphAdjacencyList:
    def __init__(self,v):
        self.verticies = []
        for i in range(v):
            self.verticies.append([])



    def add_vertex(self,vertex):
        self.verticies.append([])
    def add_edge(self,source,dest):
        verticies = self.verticies
        verticies[source].append(dest)

    def printGraph(self):
        verticies = self.verticies
        for i in range(len(verticies)):
            print(f"{i} : ", end='')
            for x in verticies[i]:
                print(x,end =' ')
            print()


graph = graphAdjacencyList(5)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(2,1)
graph.add_edge(2,0)
graph.add_vertex(6)
graph.printGraph()