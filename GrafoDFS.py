"David Hernán García Fernández - A01173130"

from pyvis.network import Network
net = Network()
net_dfs = Network()
prev = 0

class Graph:
    matrix = []

    def __init__(self, a, b):
        "constructor de la clase"
        self.a = a
        self.b = b
        Graph.matrix = [[0 for i in range(a)] for j in range(a)]
  
    def addEdge(self, start, end):
        "agregar un Edge al grafo"
        #crear la conexión en pyvis
        net.add_edge(start, end)
        Graph.matrix[start][end] = 1
  
    def DFS(self, start, seen):
        "realizar el DFS del grafo instanciado"
        print(start, end = ' ')
        seen[start] = True
        global prev
        #crear la conexión en pyvis
        net_dfs.add_edge(start, prev)
        prev=start
        for i in range(self.a):
            if (Graph.matrix[start][i] == 1 and
                    (not seen[i])):
                self.DFS(i, seen)
  
a, b = 7, 4
#Declaración de los nodos, requerido por pyvis para el grafo completo
net.add_node(0, label='A')
net.add_node(1, label='B')
net.add_node(2, label='C')
net.add_node(3, label='D')
net.add_node(4, label='E')
net.add_node(5, label='F')
net.add_node(6, label='G')

#instanciar
G = Graph(a, b)
#declarar las conexiones
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(2, 0)
G.addEdge(2, 3)
G.addEdge(3, 3)
G.addEdge(3, 0)
G.addEdge(3, 1)
G.addEdge(1, 4)
G.addEdge(2, 5)
G.addEdge(4, 5)
G.addEdge(3, 6)

#generar grafo en html usando pyvis
net.show('grafo.html')

#Declaración de los nodos, requerido por pyvis, en este caso es para el grafo del DFS
net_dfs.add_node(0, label='A')
net_dfs.add_node(1, label='B')
net_dfs.add_node(2, label='C')
net_dfs.add_node(3, label='D')
net_dfs.add_node(4, label='E')
net_dfs.add_node(5, label='F')
net_dfs.add_node(6, label='G')

visited = [False] * a
#mandar a llamar la función DFS
G.DFS(0, visited);
#generar el diagrama del DFS en html usando pyvis
net_dfs.show('dfs_graph.html')