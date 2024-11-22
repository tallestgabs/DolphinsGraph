class Graph:
    def __init__(self):
        self.nodes = {}


    def addVertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = []


    def addAdjacents(self,vertex, adjacents):
        self.addVertex(vertex)
        
        for adjacent in adjacents:
            if adjacent != vertex:  # eliminates repetitions
                self.nodes[vertex].append(adjacent)
                self.addVertex(adjacent)  # add adjacent in the graph
                self.nodes[adjacent].append(vertex)  # add vertex as adjacent because it's not directional


    def loadFile(self, file):     
        with open(file, "r") as dolphins:
            for line in dolphins:
                if line[0] == '%':  # ignores irrelevant info
                    continue
                else:
                    content = list(map(int, line.split()))
                    vertex = content[0] 
                    adjacents = content[1:]
                    

                self.addAdjacents(vertex, adjacents)



    def printVertexDegree(self):
        for vertex, adjacents in self.nodes.items():
            print(f'vertex {vertex} has degree {len(adjacents)}')



    def printMaximalsCliques(self):
        for vertex, adjacents in self.nodes.items():
            if len(adjacents) == 0:
                print(f'Vertex {vertex} is MAXIMAL and has no connections')

            elif len(adjacents) == 1:
                print(f'Vertex {vertex} is MAXIMAL and has 1 connection with {adjacents}')

            #else:
                #print(vertex, adjacents)







g = Graph()
g.loadFile("soc-dolphins.mtx")
#g.printVertexDegree()
g.printMaximalsCliques()