from collections import defaultdict, deque
from typing import Dict, List, Tuple, Set
import json


class Graph:

    
    def __init__(self, vertices: int, directed: bool = True):
        self.vertices = vertices
        self.edges = defaultdict(list)  # adjacency list: {vertex: [(neighbor, weight), ...]}
        self.directed = directed
        self.vertex_names = {i: str(i) for i in range(vertices)}  # nomes dos vértices
    
    def add_edge(self, u: int, v: int, weight: float = 1):

        self.edges[u].append((v, weight))
        
        if not self.directed:
            # Se não-direcionado, adiciona também a aresta reversa
            self.edges[v].append((u, weight))
    
    def set_vertex_name(self, vertex: int, name: str):

        if 0 <= vertex < self.vertices:
            self.vertex_names[vertex] = name
    
    def get_neighbors(self, vertex: int) -> List[Tuple[int, float]]:

        return self.edges[vertex]
    
    def get_all_vertices(self) -> List[int]:
 
        return list(range(self.vertices))
    
    def display(self):

        print("\n" + "="*60)
        print(f"GRAFO - {self.vertices} vértices - {'Direcionado' if self.directed else 'Não-direcionado'}")
        print("="*60)
        
        for vertex in range(self.vertices):
            neighbors = self.get_neighbors(vertex)
            name = self.vertex_names[vertex]
            
            if neighbors:
                edges_str = ", ".join([f"{self.vertex_names[v]}({w})" for v, w in neighbors])
                print(f"Vértice {name:>2} → {edges_str}")
            else:
                print(f"Vértice {name:>2} → (sem arestas)")
        
        print("="*60 + "\n")
    
    def save_to_json(self, filepath: str):

        data = {
            'vertices': self.vertices,
            'directed': self.directed,
            'vertex_names': self.vertex_names,
            'edges': [
                {
                    'from': u,
                    'to': v,
                    'weight': w
                }
                for u in self.edges
                for v, w in self.edges[u]
            ]
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Grafo salvo em: {filepath}")
    
    @staticmethod
    def load_from_json(filepath: str) -> 'Graph':

        with open(filepath, 'r') as f:
            data = json.load(f)
        
        g = Graph(data['vertices'], directed=data['directed'])
        g.vertex_names = {int(k): v for k, v in data['vertex_names'].items()}
        
        for edge in data['edges']:
            # Evita duplicatas em grafos não-direcionados
            if not g.directed or edge['to'] != edge['from']:
                g.add_edge(edge['from'], edge['to'], weight=edge['weight'])
        
        return g
