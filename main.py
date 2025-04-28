import math
from dataclasses import dataclass

import networkx as nx


@dataclass
class Voto:
    punti: int
    nome: str

    def __hash__(self):
        return hash((self.punti, self.nome))

    def __eq__(self, other):
        return self.nome == other.nome


grafo = nx.Graph() # grafo semplice
grafo2 = nx.DiGraph() # grafo diretto

# un nodo può essere qualsiasi oggetto Python, purchè sia hashable
grafo.add_node(1)
grafo.add_node("Due")
grafo.add_node(Voto(24, "TdP"))
grafo.add_node(math.cos)

print(grafo.nodes) # stampo nodi
print(grafo.edges) # stampo archi

grafo.add_edge("Due", 1)
print(grafo.edges)  # grafo non diretto quindi mi stampa gli archi in ordine casuale, non importa l'ordine della tupl a

grafo2.add_edge("Due", 1,  weight=0.9) # definsico anche un peso
print(grafo2.edges) # stampa nell'ordine orientato

nbunch = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grafo2.add_nodes_from(nbunch)  # aggiunge gli elementi al grafo
print(grafo2.nodes)  # se provo a riaggiungere l'oggetto 1, non viene inserito perchè già esiste nel grafo ed essendo hashable viene sovrascritto

ebunch = [(4, 6), (8, 1), (11, 9)]  # aggiunge anche il nodo 11 perchè non esiste, quindi posso anche direttamente mettere solo gli archi
grafo2.add_edges_from(ebunch)  # aggiungo una serie di archi
print(grafo2.edges)
print(grafo2.nodes)  # aggiunge anche 11

print(grafo2.get_edge_data("Due", 1))

print(grafo2["Due"])
# la chiave "Due" punta ad un altro dizionario di valori, cioè i suoi adiacenti, e i valori sono anch'essi dizionari che puntano agli attributi
# ci sono 3 dizionari annidati
print(grafo2["Due"][1])  # stampo l'attributo associato al nodo 1, avendo acceduto tramite gli adiacenti del nodo "Due"

