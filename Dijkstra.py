"David Hernán García Fernández - A01173130"

from collections import defaultdict
import sys

estaciones = ['El Rosario','Instituto del Petroleo','Tacuba','Hidalgo','Tacubaya','Centro Medico','Mixcoac','Zapata','Chabacano','Balderas',
'Salto del Agua','Bellas Artes','Guerrero','Garibaldi','La Raza','Deportivo 18 de Marzo','Martin Carrera','Consulado','Oceania','Morelos',
'San Lazaro','Pino Suarez','Candelaria','Pantitlan','Jamaica','Ermita','Santa Anita','Atlalilco']

#Class to represent a graph
class Graph():
    def extraerMin(self,dist,H):
        "extraer el mínimo"
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in H:
                minimum = dist[i]
                min_index = i
        return min_index
  
    def dijkstra(self, l, s):
        "ejecución del algoritmo de Dijkstra"
        dist = [float("Inf")] * len(l)
        prev = [-1] * len(l)
        dist[s] = 0
     
        H = []
        for i in range(len(l)):
            H.append(i)
             
        while H:
            u = self.extraerMin(dist,H)
            H.remove(u)
            for v in range(len(l[0])):
                if l[u][v] and v in H:
                    if dist[v] > dist[u] + l[u][v]:
                        dist[v] = dist[u] + l[u][v]
                        prev[v] = u 
        for i in range(1, len(dist)):
            #print("distancia desde ",estaciones[s],"a ",estaciones[i],"=",dist[i])
            print("La distancia entre ",estaciones[s]," y ",estaciones[i]," es ",dist[i])
 
g= Graph()
 """NOTA IMPORTANTE: Entre balderas y salto de agua no hay un costo y eso rompe 
el algoritmo, así que aumenté la distancia de todos en uno, por lo tanto, ahora el
costo de ir desde balderas hasta salto de agua sería 1, para ir de rosario a tacuba serían 4
y así"""
        #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27
graph = [
        [0, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#0
        [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#1
        [4, 0, 0, 7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#2
        [0, 0, 7, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#3
        [0, 0, 5, 0, 0, 3, 3, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#4
        [0, 0, 0, 0, 3, 0, 0, 4, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#5
        [0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#6
        [0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],#7
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 6, 2, 0],#8
        [0, 0, 0, 2, 6, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#9
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],#10
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],#11
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],#13
        [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#14
        [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#15
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#16
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0],#17
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0],#18
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],#19
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 1, 6, 0, 0, 0, 0],#20
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],#21
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0],#22
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 6, 0, 0, 0, 5, 0, 0, 0],#23
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 0, 0, 1, 0],#24
        [0, 0, 0, 0, 0, 0, 0, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],#25
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 6],#26
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 0]#27
        ]
 
g.dijkstra(graph,0)