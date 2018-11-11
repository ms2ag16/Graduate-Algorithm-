import heapq

def dijktras(graph , start):

    """ initialize the distances and start vertex distance"""
    visited=set([])
    vertices=set([v for v in graph])
    path={v: [v] for v in graph}

    distances={ v: float('inf') for v in graph}
    distances[start]=0
    heap = []
    for v, d in distances.items():
        entry =[d,v]
        heapq.heappush(heap, entry)

    while visited != vertices:
        curr_d, curr_v= heapq.heappop(heap)
        visited.add(curr_v)
        for neigh_v, neigh_d in graph[curr_v].items():
            distance=distances[curr_v] + neigh_d
            if distance < distances[neigh_v]:
                path[neigh_v]=path[curr_v]+[neigh_v]
                distances[neigh_v]=distance
        print ("visited=", visited)
        print ("path=", path)
    return distances



if __name__=="__main__":
    example_graph = {
        'U': {'V': 2, 'W': 5, 'X': 1},
        'V': {'U': 2, 'X': 2, 'W': 3},
        'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
        'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
        'Y': {'X': 1, 'W': 1, 'Z': 1},
        'Z': {'W': 5, 'Y': 1},
    }
    print (dijktras(example_graph, 'X'))
