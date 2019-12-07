import random
from Queue import PriorityQueue


# function to compute manhattan distance between a data point 'vertex' and query point 'q'
def compute_manhattan_distance(q, vertex):
    abs_dist = 0
    for i in range(4):
        abs_dist += abs(float(q.features[i]) - float(vertex.features[i]))
    return abs_dist


def knn_search(knn_graph, d, m, k):
    # temp_set = []
    neighbor_set = PriorityQueue()
    visited_set = []
    result = PriorityQueue()

    # m searches are needed
    for i in range(m):
        random_vertex_index = random.randint(0, len(knn_graph)-1)
        random_vertex = list(knn_graph)[random_vertex_index]
        random_vertex.dist = compute_manhattan_distance(d, random_vertex)
        neighbor_set.put((random_vertex.dist, random_vertex))
        temp_set = []
        while True:
            cn = neighbor_set.get()
            closest_neighbor = cn[1]
            print "cn", closest_neighbor
            closest_neighbor.dist = compute_manhattan_distance(d, closest_neighbor)
            # get kth smallest element from result, i.e., element at (k-1)th position in result
            temp_result = []
            kth_element = None
            if not result.empty():
                # pop 0 to k-2 elements
                for j in range(k-1):
                    temp_result.append(result.get())
                # get (k-1)th element
                e = result.get()
                kth_element = e[1]
                kth_element.dist = compute_manhattan_distance(d, kth_element)
                # push back popped elements into result
                for j in range(len(temp_result)):
                    result.put(temp_result[j])
                result.put(kth_element)
            # check stop condition
            if kth_element is not None and closest_neighbor.dist > kth_element.dist:
                # update neighbor_set
                neighbor_set.put((kth_element.dist, kth_element))
                break

            neighbors_of_closest_neighbor = knn_graph[closest_neighbor]
            for neighbor in neighbors_of_closest_neighbor:
                # print neighbor
                neighbor.dist = compute_manhattan_distance(d, neighbor)
                visited_set.append(neighbor)
                neighbor_set.put((neighbor.dist, neighbor))
                temp_set.append(neighbor)
            break

        for data_point in temp_set:
            result.put((data_point.dist, data_point))
        break

    # return the k neighbors of query point
    k_neighbors = []
    for i in range(k):
        neighbor = result.get()
        k_neighbors.append(neighbor[1])
    return k_neighbors
