import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    
    #inicia dicionario para armazenar vertices e suas adjacencias
    def __init__(self):
        self.nodes = {}


    #adiciona vertice ao grafo, caso ele ainda nao exista
    def addVertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = []



    #adiciona "arestas" entre vertice e adjacentes
    def addAdjacents(self, vertex, adjacents):
        self.addVertex(vertex)
        for adjacent in adjacents:
            if adjacent != vertex and adjacent not in self.nodes[vertex]:
                self.nodes[vertex].append(adjacent)
                self.addVertex(adjacent)
                self.nodes[adjacent].append(vertex) #relacao bidirecional



    #carrega arquivo e formata para os tipos certos
    def loadFile(self, file):
        with open(file, "r") as dolphins:
            for line in dolphins:
                if line[0] == "%":  # Ignora linhas inuteis
                    continue
                content = list(map(int, line.split()))
                vertex = content[0]
                adjacents = content[1:]
                self.addAdjacents(vertex, adjacents)


    #imprime o grau de cada vertice
    def printVertexDegree(self):
        print("Vertex's Degree")
        for vertex, adjacents in self.nodes.items():
            print(f"Vertex {vertex}: Degree -> {len(adjacents)}")




    #calcula o coeficiente de agrupamento para cada vertice
    def calculateVertexClustering(self):
        print("\nVertex Clustering Coefficient:")
        clustering = {}
        for vertex, adjacents in self.nodes.items():
            #se um vertice tiver menos que 2 adjacentes, o coeficiente e 0
            if len(adjacents) < 2:
                clustering[vertex] = 0.0
                continue
            #conexoes possiveis entre adjacentes
            possibleConnections = len(adjacents) * (len(adjacents) - 1) / 2
            #conexoes reais entre adjacentes
            currentConnections = sum(
                1 for u in adjacents for v in adjacents if u != v and v in self.nodes[u]
            ) /2 #divide para evitar duplicacao

            #calcula o coeficiente de agrupamento
            clustering[vertex] = currentConnections / possibleConnections
            print(f"Vertex {vertex}: {clustering[vertex]:.3f}")
        return clustering
    


    #calcula o coeficiente de agrupamento medio do grafo
    def averageClustering(self):
        clustering = self.calculateVertexClustering() #coeficiente de cada vertice
        avg_clustering = sum(clustering.values()) / len(clustering) #media dos valores
        print(f"\nGraph's average clustering coefficient: {avg_clustering:.3f}")
        return avg_clustering


    #algoritmo Bron-Kerbosch para encontrar cliques maximos
    def bronKerbosch(self, R, P, X, cliques):
        if not P and not X:
            #se nao tiver mais vertices para explorar, adiciona o clique formado
            cliques.append(R)
            return
        for vertex in list(P): #caminha pelos vertices em P
            adjacents = set(self.nodes[vertex]) #vertices adjacentes ao atual

            #recursao com o vertice adicionado ao clique atual
            self.bronKerbosch(
                R.union({vertex}),
                P.intersection(adjacents),
                X.intersection(adjacents),
                cliques,
            )

            #apos explorar move de P para X
            P.remove(vertex)
            X.add(vertex)




    #encontra e imprime os cliques maximos do grafo
    def maximalCliques(self):
        print("\nMaximal Cliques:")
        cliques = []
        P = set(self.nodes.keys()) #vertices do grafo
        self.bronKerbosch(set(), P, set(), cliques) #inicia o algoritmo
        for clique in cliques:
            print(f"Clique with {len(clique)} vertex: {sorted(clique)}")
        return cliques




    #vizualizacao do grafo
    def visualizeGraph(self, cliques):
        print("\nPlotting the Graph...")
        print("Attention! if you are in a virtual environment the command plt.show will not work",
              "the function will save the graph.png on the file directory, just open it")

        G = nx.Graph() #cria grafo usando networkx
        
        #adiciona as arestas ao grafo
        for vertex, adjacentes in self.nodes.items():
            for adjacente in adjacentes:
                G.add_edge(vertex, adjacente)

        # Atribui cores aos cliques
        colors = plt.cm.rainbow([i / len(cliques) for i in range(len(cliques))])
        color_map = {}
        for i, clique in enumerate(cliques):
            for node in clique:
                color_map[node] = colors[i] #associa uma cor a cada clique

        #define as cores / preto como padrao para os que estao fora dos cliques
        node_colors = [color_map.get(node, (0, 0, 0, 1)) for node in G.nodes]
        pos = nx.spring_layout(G, seed=42, k=3)  

        #desenha o grafo
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color=node_colors,
            edge_color="gray",
            node_size=400,
            font_size=10,
        )

        #salva e exibe o grafo
        plt.savefig("DolphinGraph.png")
        plt.show()


g = Graph()
g.loadFile("soc-dolphins.mtx")  
g.printVertexDegree()
cliques = g.maximalCliques()
g.averageClustering()
g.visualizeGraph(cliques)
