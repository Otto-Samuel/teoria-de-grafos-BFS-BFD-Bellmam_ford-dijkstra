from collections import deque
from typing import List, Dict, Tuple, Set


class BFS:
  
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.parent = {}
        self.distance = {}
        self.execution_order = []  # ordem de visita dos vértices
    
    def search(self, start: int) -> List[int]:
        self.visited = set()
        self.parent = {start: None}
        self.distance = {start: 0}
        self.execution_order = []
        
        queue = deque([start])
        self.visited.add(start)
        
        while queue:
            # Passo 1: Remove vértice da fila (FIFO)
            vertex = queue.popleft()
            self.execution_order.append(vertex)
            
            # Passo 2: Explora todos os vizinhos
            for neighbor, _ in self.graph.get_neighbors(vertex):
                if neighbor not in self.visited:
                    # Passo 3: Marca como visitado e adiciona à fila
                    self.visited.add(neighbor)
                    self.parent[neighbor] = vertex
                    self.distance[neighbor] = self.distance[vertex] + 1
                    queue.append(neighbor)
        
        return self.execution_order
    
    def find_shortest_path(self, start: int, end: int) -> Tuple[bool, List[int]]:

        self.search(start)
        
        if end not in self.visited:
            return False, []
        
        # Reconstrói o caminho usando os pais
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.parent.get(current)
        
        path.reverse()
        return True, path
    
    def get_level_order(self, start: int) -> Dict[int, List[int]]:

        self.search(start)
        
        levels = {}
        for vertex, dist in self.distance.items():
            if dist not in levels:
                levels[dist] = []
            levels[dist].append(vertex)
        
        return dict(sorted(levels.items()))
    
    def display_result(self, start: int):

        self.search(start)
        
        print("\n" + "="*70)
        print("RESULTADO DA BUSCA EM AMPLITUDE (BFS)")
        print("="*70)
        print(f"Vértice inicial: {self.graph.vertex_names[start]}")
        print(f"Ordem de visita: {' → '.join([self.graph.vertex_names[v] for v in self.execution_order])}")
        
        print("\nNíveis (distância do vértice inicial):")
        levels = self.get_level_order(start)
        for level, vertices in levels.items():
            vertices_names = [self.graph.vertex_names[v] for v in vertices]
            print(f"  Nível {level}: {', '.join(vertices_names)}")
        
        print("\n" + "="*70 + "\n")


class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.parent = {}
        self.discovery_time = {}
        self.finish_time = {}
        self.execution_order = []
        self.time_counter = 0
    
    def search(self, start: int) -> List[int]:
        self.visited = set()
        self.parent = {}
        self.discovery_time = {}
        self.finish_time = {}
        self.execution_order = []
        self.time_counter = 0
        
        self._dfs_recursive(start)
        
        return self.execution_order
    
    def _dfs_recursive(self, vertex: int):
        # Passo 1: Marca como visitado
        self.visited.add(vertex)
        self.execution_order.append(vertex)
        self.time_counter += 1
        self.discovery_time[vertex] = self.time_counter
        
        # Passo 2: Explora todos os vizinhos
        for neighbor, _ in self.graph.get_neighbors(vertex):
            if neighbor not in self.visited:
                self.parent[neighbor] = vertex
                # Passo 3: Chamada recursiva
                self._dfs_recursive(neighbor)
        
        # Passo 4: Marca tempo de conclusão
        self.time_counter += 1
        self.finish_time[vertex] = self.time_counter
    
    def search_iterative(self, start: int) -> List[int]:
        self.visited = set()
        self.parent = {}
        self.execution_order = []
        
        stack = [start]
        self.visited.add(start)
        
        while stack:
            # Passo 1: Remove vértice do topo da pilha
            vertex = stack.pop()
            self.execution_order.append(vertex)
            
            # Passo 2: Explora vizinhos (adiciona em ordem reversa para manter ordem)
            neighbors = self.graph.get_neighbors(vertex)
            for neighbor, _ in reversed(neighbors):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.parent[neighbor] = vertex
                    stack.append(neighbor)
        
        return self.execution_order
    
    def find_path(self, start: int, end: int) -> Tuple[bool, List[int]]:
        self.search(start)
        
        if end not in self.visited:
            return False, []
        
        # Reconstrói o caminho usando os pais
        path = []
        current = end
        visited_in_path = set()
        
        while current is not None and current not in visited_in_path:
            path.append(current)
            visited_in_path.add(current)
            current = self.parent.get(current)
        
        path.reverse()
        return True, path
    
    def detect_cycle(self) -> bool:
        visited = set()
        rec_stack = set()  # pilha de recursão
        
        def has_cycle_util(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor, _ in self.graph.get_neighbors(vertex):
                if neighbor not in visited:
                    if has_cycle_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in range(self.graph.vertices):
            if vertex not in visited:
                if has_cycle_util(vertex):
                    return True
        
        return False
    
    def display_result(self, start: int):
        self.search(start)
        
        print("\n" + "="*70)
        print("RESULTADO DA BUSCA EM PROFUNDIDADE (DFS)")
        print("="*70)
        print(f"Vértice inicial: {self.graph.vertex_names[start]}")
        print(f"Ordem de visita: {' → '.join([self.graph.vertex_names[v] for v in self.execution_order])}")
        
        print("\nTempo de descoberta e conclusão:")
        sorted_vertices = sorted(self.discovery_time.keys())
        for vertex in sorted_vertices:
            print(f"  {self.graph.vertex_names[vertex]}: " 
                  f"descoberta={self.discovery_time[vertex]}, "
                  f"conclusão={self.finish_time[vertex]}")
        
        print(f"\nCiclo detectado: {'Sim' if self.detect_cycle() else 'Não'}")
        
        print("\n" + "="*70 + "\n")
