from collections import deque
from typing import List, Dict, Tuple

def AugmentedHierholzer(G: Dict[str, List[str]], start: str) -> Tuple[List[str], List[List[str]]]:
    """
    Args:
        G (dict): Adjacency matrix implemented as dictionary.
        start (str): Starting node for the algorithm.
    Returns:
        Tuple[List[str], List[List[str]]]: A tuple containing path in Euler graph.
    """
    stack = deque()
    stack.append(start)
    
    cycle = []
    circles = []
    
    while stack:
        u = stack[-1]
        adj = G[u]
        if len(adj) > 0:
            v = G[u][0]
            stack.append(v)
            G[u].remove(v)
            G[v].remove(u)
        else:
            cycle.append(stack[-1])
            circlestart = cycle[-1]
            for i in range(len(cycle)-2, -1, -1):
                if cycle[i] == circlestart:
                    circles.append(cycle[i:])
                    break
            del cycle[-1]

            if len(stack) > 1:
                cycle.append(stack[-1])
            stack.pop()
            
    cycle.append(start)

    #indexes = []
    #for i in set(cycle):
    #    this = [j for j, x in enumerate(cycle) if x == i]
    #    for i in range(len(this)-1):
    #        indexes.append(this[i:i+2][::-1])

    #for i in sorted(indexes):
    #    circles.append(cycle[i[1]:i[0]+1])

    return cycle, circles






import copy

G = {'a': ['b', 'c', 'd', 'e'],
     'b': ['a', 'd', 'e'],
     'c': ['a', 'e'],
     'd': ['a', 'b', 'e'],
     'e': ['a', 'b', 'c', 'd']}
     
G1 = copy.deepcopy(G)

path, circles = AugmentedHierholzer(G1, 'b')
path.reverse()

assert path == ['b', 'a', 'c', 'e', 'a', 'd', 'b', 'e', 'd']
assert circles == [['d', 'e', 'b', 'd'], ['e', 'b', 'd', 'a', 'e'], ['a', 'e', 'c', 'a'], ['b', 'd', 'a', 'e', 'c', 'a', 'b']]

G1 = copy.deepcopy(G)

path, circles = AugmentedHierholzer(G1, 'd')
path.reverse()

assert path == ['d', 'a', 'b', 'd', 'e', 'a', 'c', 'e', 'b']
assert circles == [['e', 'c', 'a', 'e'], ['b', 'e', 'c', 'a', 'e', 'd', 'b'], ['a', 'e', 'd', 'b', 'a'], ['d', 'b', 'a', 'd']]









