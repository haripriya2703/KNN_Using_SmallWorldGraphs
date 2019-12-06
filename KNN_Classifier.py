from KNN_Search import knn_search


def knn_classifier(knn_graph, d, m, k):
    species_labels = ['setosa', 'virginica', 'versicolor']
    labels_count = [0, 0, 0]
    # if data point is a vertex in the graph, get its neighbors from the adjacency list representation of the graph
    if d in knn_graph:
        print "d.id", d.id
        neighbors = knn_graph[d]
    # if data point is not a vertex, invoke knn_search to get neighbors
    else:
        neighbors = knn_search(knn_graph, d, m, k)
    for neighbor in neighbors:
        for i in range(3):
            if neighbor.label == species_labels[i]:
                labels_count[i] += 1
                break
    label = species_labels[labels_count.index(max(labels_count))]
    return label

