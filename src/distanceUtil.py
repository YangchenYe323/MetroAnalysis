from typing import List
from copy import deepcopy
from math import sqrt

def get_distance_matrix(edge_matrix: List[List[int]]) -> List[List[int]]:
    '''
    given a graph, calculate the shortest path for each pair of nodes
    using floyd warshel algorithm
    '''
    distance_matrix = deepcopy(edge_matrix)
    n = len(distance_matrix)
    for middle in range(n):
        for start in range(n):
            for dest in range(n):
                distance_matrix[start][dest] = \
                    min(distance_matrix[start][dest], distance_matrix[start][middle] + distance_matrix[middle][dest])
    
    return distance_matrix

def geometric_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return _normalize(sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)))

def _normalize(num: float) -> float:
    return num * 1000