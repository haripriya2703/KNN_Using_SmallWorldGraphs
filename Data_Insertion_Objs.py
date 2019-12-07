from KNN_Search import knn_search


def knn_data_insertion(knn_graph, d, m, k):
    knn_graph[d] = []
    # neighbor_ids = []

    # if there are already k+1 data points in the graph, k neighbors are found by invoking knn_search
    if len(knn_graph) > k+1:
        neighbors = knn_search(knn_graph, d, m, k)
        # Add the new data point in the graph and add edges to the neighbors
        # for neighbor in neighbors:
        #     neighbor_ids.append(neighbor.id)

        # Add edges between vertices and data point
        for neighbor in neighbors:
            if neighbor != d:
                knn_graph[neighbor].append(d)
                knn_graph[d].append(neighbor)

    # if there are less than k+1 data points, edges are added between all vertices and the data point
    else:
        # Add edges between vertices and data point
        if len(knn_graph) > 1:
            for neighbor in knn_graph:
                if neighbor != d:
                    knn_graph[neighbor].append(d)
                    knn_graph[d].append(neighbor)

    # print "list", dict(knn_graph)
    return knn_graph



