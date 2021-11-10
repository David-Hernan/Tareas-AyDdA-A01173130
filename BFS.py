"David Hernán García Fernández - A01173130"

from collections import defaultdict

estaciones = ['El Rosario','Instituto del Petroleo','Tacuba','Hidalgo','Tacubaya','Centro Medico','Mixcoac','Zapata','Chabacano','Balderas',
'Salto del Agua','Bellas Artes','Guerrero','Garibaldi','La Raza','Deportivo 18 de Marzo','Martin Carrera','Consulado','Oceania','Morelos',
'San Lazaro','Pino Suarez','Candelaria','Pantitlan','Jamaica','Ermita','Santa Anita','Atlalilco']
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    def __init__(self):
        "constructor de la clase"
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        "agregar un Edge al grafo"
        self.graph[u].append(v)
 
    def BFS(self, s):
        "realizar el BFS del grafo instanciado"
        dist = []
        for i in range(100):
            dist.append(0)
            
        dist[s]=0
        queue = []
 
        visited = [False] * (max(self.graph) + 1)
 
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for v in self.graph[s]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True
                    dist[v]=dist[s]+1
        print("\nDesde El Rosario:")
        for i in range(28):
            print("distancia a ",estaciones[i],"=",dist[i])
 

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(5, 9)
g.addEdge(9, 3)
g.addEdge(6, 7)
g.addEdge(4, 9)
g.addEdge(9, 10)
g.addEdge(3, 11)
g.addEdge(3, 12)
g.addEdge(12, 13)
g.addEdge(13, 11)
g.addEdge(12, 14)
g.addEdge(14, 1)
g.addEdge(1, 15)
g.addEdge(14, 15)
g.addEdge(15, 16)
g.addEdge(14, 17)
g.addEdge(17, 16)
g.addEdge(17, 18)
g.addEdge(17, 19)
g.addEdge(19, 13)
g.addEdge(19, 20)
g.addEdge(11, 10)
g.addEdge(11, 21)
g.addEdge(21, 10)
g.addEdge(21, 22)
g.addEdge(22, 19)
g.addEdge(22, 20)
g.addEdge(20, 18)
g.addEdge(18, 23)
g.addEdge(20, 23)
g.addEdge(23, 24)
g.addEdge(24, 22)
g.addEdge(24, 8)
g.addEdge(8, 21)
g.addEdge(8, 10)
g.addEdge(8, 25)
g.addEdge(8, 26)
g.addEdge(26, 24)
g.addEdge(7, 25)
g.addEdge(25, 27)
g.addEdge(27, 26)
 
print ("BFT:")
#g.BFS('El Rosario')
g.BFS(0)

