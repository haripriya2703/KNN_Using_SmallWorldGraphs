from KNN_Search import knn_search


def knn_data_insertion(knn_graph, distance_metric, d, m, k):
    """
    :param knn_graph: existing graph
    :param distance_metric: metric using which the nearest neighbors should be determined
    :param d: new data point
    :param m: number of searches to be performed
    :param k: number of neighbors to be searched for
    :return: updated graph after insertion of new data point
    """
    knn_graph[d] = []
    # neighbor_ids = []

    # if there are already k+1 data points in the graph, k neighbors are found by invoking knn_search
    if len(knn_graph) > k+1:
        neighbors = knn_search(knn_graph, distance_metric, d, m, k)

        # Add edges between vertices and data point
        for neighbor in neighbors:
            if neighbor != d:
                knn_graph[neighbor].append(d)
                knn_graph[d].append(neighbor)

    # if there are less than k+1 data points, edges are added between all vertices and the data point
    else:
        # Add edges between vertices and data point
        # print "Inserting the data point number: ", len(knn_graph)+1
        if len(knn_graph) > 1:
            for neighbor in knn_graph:
                if neighbor != d:
                    knn_graph[neighbor].append(d)
                    knn_graph[d].append(neighbor)

    return knn_graph
