from KNN_Search import knn_search


def knn_classifier(knn_graph, d, m, k, labels):
    species_labels = ['setosa', 'virginica', 'versicolor']
    labels_count = [0, 0, 0]
    # if data point is a vertex in the graph, get its neighbors from the adjacency list representation of the graph
    if d.id in knn_graph:
        print "d.id", d.id
        neighbors = knn_graph[d.id]
    # if data point is not a vertex, invoke knn_search to get neighbors
    else:
        neighbor_objects = knn_search(knn_graph, d, m, k)
        neighbors = []
        for neighbor in neighbor_objects:
            neighbors.append(neighbor.id)
    for neighbor in neighbors:
        for i in range(3):
            if labels[neighbor] == species_labels[i]:
                labels_count[i] += 1
                break
    label = species_labels[labels_count.index(max(labels_count))]
    return label

