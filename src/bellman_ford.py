
from typing import Dict, List, Tuple, Optional


def bellman_ford(graph, source: int) -> Tuple[Optional[Dict[int, float]], Optional[Dict[int, Optional[int]]]]:

    vertices = graph.vertices()
    dist: Dict[int, float] = {v: float('inf') for v in vertices}
    parent: Dict[int, Optional[int]] = {v: None for v in vertices}
    dist[source] = 0.0
    n = len(vertices)
    edges = graph.edges()
    
    for i in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break
    
    # Verificar ciclo negativo
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            # Ciclo negativo detectado
            return None, None
    
    return dist, parent
