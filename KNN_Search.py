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
    for i in range(m):
        vertices = knn_graph.keys()
        random_vertex_index = random.randint(0, len(vertices)-1)
        random_vertex = vertices[random_vertex_index]
        random_vertex.dist = compute_manhattan_distance(d, random_vertex)
        neighborset.put((random_vertex.dist, random_vertex))
        tempset = []
        while True:
            closest_neighbor = neighborset.get()
            if 5:# stop condition:
                # break
                # update neighborset
            neighbors_of_closest_neighbor = knn_graph[closest_neighbor.id]
            for neighbor in neighbors_of_closest_neighbor:
                neighbor.dist = compute_manhattan_distance(d, neighbor)
                visitedset.append(neighbor)
                neighborset.put((neighbor.distance, neighbor))
                tempset.append(neighbor)
            break
        for data_point in tempset:
            result.put((data_point.dist, data_point))
        break

    # return the k neighbors
    k_neighbors = []
    for i in range(k):
        k_neighbors.append(result.get())
    return k_neighbors