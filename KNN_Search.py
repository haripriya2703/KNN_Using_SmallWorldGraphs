import random
import math
from Queue import PriorityQueue


# function to compute manhattan distance between a data point 'vertex' and query point 'q'
def compute_manhattan_distance(q, vertex):
    """
    :param q: query point
    :param vertex: some vertex in the graph
    :return: manhattan distance between the two points
    """
    abs_dist = 0
    for i in range(4):
        abs_dist += abs(float(q.features[i]) - float(vertex.features[i]))
    return abs_dist


# function to compute euclidean distance between a data point 'vertex' and query point 'q'
def compute_euclidean_distance(q, vertex):
    """
    :param q: query point
    :param vertex: some vertex in the graph
    :return: euclidean distance between the two points
    """
    euclidean_dist = 0
    for i in range(len(q.features)):
        euclidean_dist += (float(q.features[i]) - float(vertex.features[i]))**2
    return math.sqrt(euclidean_dist)


def knn_search(knn_graph, d, m, k):
    """
    :param knn_graph: existing graph
    :param d: new data point
    :param m: number of searches to be performed
    :param k: number of neighbors to be searched for
    :return: a list of k neighbors for the data point d
    """

    neighbor_set = PriorityQueue()
    non_visited_set = set(knn_graph) - {d}
    result = PriorityQueue()

    # m searches are needed
    for i in range(m):
        # print "non-visited set: ", d.id, non_visited_set
        if len(non_visited_set) == 0:
            break
        elif len(non_visited_set) == 1:
            random_vertex_index = 0
        else:
            random_vertex_index = random.randint(0, len(non_visited_set)-1)
        random_vertex = list(non_visited_set)[random_vertex_index]
        print "search number: ", i, " random vertex chosen", random_vertex.id
        # print "knn_graph size ", list(knn_graph)

        random_vertex.dist = compute_euclidean_distance(d, random_vertex)
        neighbor_set.put((random_vertex.dist, random_vertex))
        temp_set = PriorityQueue()

        while True:
            if neighbor_set.qsize() == 0:
                break
            cn = neighbor_set.get()
            closest_neighbor = cn[1]
            # print "cn", closest_neighbor.id

            closest_neighbor.dist = cn[0]
            # closest_neighbor.dist = compute_manhattan_distance(d, closest_neighbor)
            # print "closest_neighbor distance from data point", closest_neighbor.dist

            # get kth smallest element from result, i.e., element at (k-1)th position in result
            temp_result = []
            kth_element = None

            if temp_set.qsize() >= k:
                # pop 0 to k-2 elements
                for j in range(k-1):
                    temp_result.append(temp_set.get())
                # get (k-1)th element
                e = temp_set.get()
                kth_element = e[1]
                kth_element.dist = e[0]
                # kth_element.dist = compute_manhattan_distance(d, kth_element)
                # push back popped elements into result
                for element in temp_result:
                    temp_set.put((element[0], element[1]))
                temp_set.put((kth_element.dist, kth_element))

            # check stop condition
            if kth_element is not None and closest_neighbor.dist > kth_element.dist:
                # update neighbor_set
                ##### neighbor_set.put((kth_element.dist, kth_element))
                break

            neighbors_of_closest_neighbor = knn_graph[closest_neighbor]
            for neighbor in neighbors_of_closest_neighbor:
                # print neighbor
                # visited_set.append(neighbor)
                if neighbor in non_visited_set:
                    non_visited_set.remove(neighbor)

                    neighbor.dist = compute_manhattan_distance(d, neighbor)
                    neighbor_set.put((neighbor.dist, neighbor))
                    temp_set.put((neighbor.dist, neighbor))

        for data_point in temp_set.queue:
            result.put((data_point[0], data_point[1]))
        # print "Testing the result: ", result.queue

    print "for loop broken, appending temp result to result"
    # return the k neighbors of query point
    k_neighbors = []
    for i in range(k):
        neighbor = result.get()
        k_neighbors.append(neighbor[1])
    # print len(k_neighbors)
    return k_neighbors
