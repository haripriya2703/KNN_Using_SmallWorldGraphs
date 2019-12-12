from KNN_Search import knn_search


def knn_classifier(knn_graph, distance_metric, d, m, k):
    """
    :param knn_graph: existing graph
    :param distance_metric: metric using which the nearest neighbors should be determined
    :param d: new data point
    :param m: number of searches to be performed
    :param k: number of neighbors to be searched for
    :return: predicted label for the data point based on k-nearest neighbors
    """
    species_labels = ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor']
    labels_count = [0, 0, 0]

    # if data point is a vertex in the graph, get its neighbors from the adjacency list representation of the graph
    if d in knn_graph:
        return knn_graph[d].label

    # if data point is not a vertex, invoke knn_search to get neighbors
    neighbors = knn_search(knn_graph, distance_metric, d, m, k)

    for neighbor in neighbors:
        for i in range(3):
            if neighbor.label == species_labels[i]:
                labels_count[i] += 1
                break

    label_index = labels_count.index(max(labels_count))
    label = species_labels[label_index]
    return label_index, label
