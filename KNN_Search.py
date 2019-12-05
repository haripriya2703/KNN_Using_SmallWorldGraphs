import random
from Queue import PriorityQueue
def compute_manhattan_distance(d, vertex):
    abs_dist = 0
    for i in range(4):
        abs_dist += abs(d.features[i] - vertex.features[i])
    return abs_dist

def knn_search(knn_graph, d, m, k):
    tempset = []
    neighborset = PriorityQueue()
    visitedset = []
    result = PriorityQueue()

    # m searches are needed
    for i  in range(m):
        vertices = knn_graph.keys()
        random_vertex_index = random.randint(0, len(vertices)-1)
        random_vertex = vertices[random_vertex_index]
        distance = compute_manhattan_distance(d, random_vertex)
        neighborset.put((distance, random_vertex))
        tempset = []
        while True:
            closest_neighbor = neighborset.get()



    closest
    neighbor =
    from neighbor set, get
    vertex
    closest
    to
    q
    neighbor
    set.delete(closest
    neighbor)//check
    stop
    condition: if closest neighbor is further than kth element from result break repeat update neighbor set for each neighbor n of closest neighbor do: if
    n is not present in visited
    set
    visited
    set.append(n)
    neighbor
    set.append(n)
    temp
    set.append(n)
    end
    repeat
    add
    vertices
    from temp set
    into
    result
    end
    for loop return k closest elements from result