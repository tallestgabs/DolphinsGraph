import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.nodes = {}


    def addVertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes[vertex] = []



    def addAdjacents(self, vertex, adjacents):
        self.addVertex(vertex)
        for adjacent in adjacents:
            if adjacent != vertex and adjacent not in self.nodes[vertex]:
                self.nodes[vertex].append(adjacent)
                self.addVertex(adjacent)
                self.nodes[adjacent].append(vertex)




    def loadFile(self, file):
        with open(file, "r") as dolphins:
            for line in dolphins:
                if line[0] == "%":  # Ignora linhas inuteis
                    continue
                content = list(map(int, line.split()))
                vertex = content[0]
                adjacents = content[1:]
                self.addAdjacents(vertex, adjacents)



    def printVertexDegree(self):
        print("Vertex's Degree")
        for vertex, adjacents in self.nodes.items():
            print(f"Vertex {vertex}: Degree -> {len(adjacents)}")





    def calculateVertexClustering(self):
        print("\nVertex Clustering Coefficient:")
        clustering = {}
        for vertex, adjacents in self.nodes.items():
            if len(adjacents) < 2:
                clustering[vertex] = 0.0
                continue
            possibleConnections = len(adjacents) * (len(adjacents) - 1) / 2
            currentConnections = sum(
                1 for u in adjacents for v in adjacents if u != v and v in self.nodes[u]
            ) /2
            clustering[vertex] = currentConnections / possibleConnections
            print(f"Vertex {vertex}: {clustering[vertex]:.3f}")
        return clustering
    



    def averageClustering(self):
        clustering = self.calculateVertexClustering()
        avg_clustering = sum(clustering.values()) / len(clustering)
        print(f"\nGraph's average clustering coefficient: {avg_clustering:.3f}")
        return avg_clustering


    def bronKerbosch(self, R, P, X, cliques):
        if not P and not X:
            cliques.append(R)
            return
        for vertex in list(P):
            adjacents = set(self.nodes[vertex])
            self.bronKerbosch(
                R.union({vertex}),
                P.intersection(adjacents),
                X.intersection(adjacents),
                cliques,
            )
            P.remove(vertex)
            X.add(vertex)




    def maximalCliques(self):
        print("\nMaximal Cliques:")
        cliques = []
        P = set(self.nodes.keys())
        self.bronKerbosch(set(), P, set(), cliques)
        for clique in cliques:
            print(f"Clique with {len(clique)} vertex: {sorted(clique)}")
        return cliques





    def visualizeGraph(self, cliques):
        print("\Plotting the Graph...")
        print("Attention! if you are in a virtual environment the command plt.show will not work",
              "the function will save the graph.png on the file directory, just open it")
        G = nx.Graph()
        for vertex, adjacentes in self.nodes.items():
            for adjacente in adjacentes:
                G.add_edge(vertex, adjacente)

        # Atribui cores aos cliques
        colors = plt.cm.rainbow([i / len(cliques) for i in range(len(cliques))])
        color_map = {}
        for i, clique in enumerate(cliques):
            for node in clique:
                color_map[node] = colors[i]

        node_colors = [color_map.get(node, (0, 0, 0, 1)) for node in G.nodes]
        pos = nx.spring_layout(G, seed=42)  
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color=node_colors,
            edge_color="gray",
            node_size=500,
            font_size=10,
        )
        plt.savefig("DolphinGraph.png")
        plt.show()


g = Graph()
g.loadFile("soc-dolphins.mtx")  
g.printVertexDegree()
g.averageClustering()
cliques = g.maximalCliques()
g.visualizeGraph(cliques)
