from KNN_Search import knn_search


def knn_classifier(knn_graph, d, m, k):
    species_labels = ['setosa', 'virginica', 'versicolor']
    labels_count = [0, 0, 0]
    d.neighbors = knn_search(knn_graph, d, m, k)
    for neighbor in d.neighbors:
        for i in range(3):
            if neighbor.label == species_labels[i]:
                labels_count[i] += 1
                break
    d.label = species_labels[labels_count.index(max(labels_count))]
    return d.label

