from KNN_Search import knn_search


def knn_data_insertion(knn_graph, d, m, k):
    neighbors = knn_search(knn_graph, d, m, k)

    # Add the new data point in the graph and add edges to the neighbors
    knn_graph[d.key] = neighbors

    # Add edge from all the neighbors to the new data point
    for neighbor in neighbors:
        current_neighbors = knn_graph[neighbor.id]
        current_neighbors.append(d.id)
