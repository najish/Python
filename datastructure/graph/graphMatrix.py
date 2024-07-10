class graphMatrix:
    def __init__(self,v):
        self.matrix = []
        for i in range(v):
            list = []
            for j in range(v):
                list.append(0)
            self.matrix.append(list)


    def add_vertex(self):
    def add_edge(self,source,dest):
        matrix = self.matrix
        matrix[source][dest] = 1

    def printGraph(self):
        for i in range(len(self.matrix)):
            list = self.matrix[i]
            print(f"{i} : ", end = ' ')
            for x in list:
                print(x, end=' ')
            print()



if __name__ == "__main__":
    graph = graphMatrix(5)
    graph.add_edge(2,4)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(0,3)
    graph.add_edge(0,4)
    graph.printGraph()