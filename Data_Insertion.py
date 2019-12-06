from KNN_Search import knn_search


def knn_data_insertion(knn_graph, d, m, k):
    knn_graph[d.id] = []
    # if there are already k+1 data points in the graph, k neighbors are found by invoking knn_search
    if len(knn_graph) > k+1:
        neighbors = knn_search(knn_graph, d, m, k)
        # Add the new data point in the graph and add edges to the neighbors
        # for neighbor in neighbors:
        #     neighbor_ids.append(neighbor.id)

        # Add edges between vertices and data point
        for neighbor in neighbors:
            knn_graph[neighbor.id].append(d.id)
            knn_graph[d.id].append(neighbor.id)
    # if there are less than k+1 data points, edges are added between all vertices and the data point
    else:
        # Add edges between vertices and data point
        for neighbor in knn_graph:
            knn_graph[neighbor.id].append(d.id)
            knn_graph[d.id].append(neighbor.id)

    return knn_graph



