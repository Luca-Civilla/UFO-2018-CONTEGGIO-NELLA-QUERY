import copy
import math
import geopy

import networkx as nx
from geopy.distance import geodesic

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()

    def buildGraph(self,anno,giorni):
        self._stati = DAO.getStates()
        self._grafo.add_nodes_from(self._stati)
        self._creaArchi(anno,giorni)

    def _creaArchi(self,anno,giorni):
        self._grafo.clear_edges()
        vicini = DAO.getNeighbors()
        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                if u!= v:
                    for vici in vicini:
                        if u.id == vici[0] and v.id== vici[1]:
                            tab = DAO.getPeso(u.id,v.id,anno,giorni)
                            peso = tab[0]
                            self._grafo.add_edge(u,v,weight= peso)

    def sommaPesiArchi(self):
        lista= []
        for node in self._grafo.nodes:
            punteggio = 0
            for vicino in self._grafo.neighbors(node):
                punteggio+=self._grafo[node][vicino]["weight"]
            lista.append((node,punteggio))
        return lista

    def graphDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)
