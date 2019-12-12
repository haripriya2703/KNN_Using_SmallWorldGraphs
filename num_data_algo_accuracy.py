from Data_Insertion_Objs import knn_data_insertion
from KNN_Search import knn_search
from KNN_Search import compute_euclidean_distance
from KNN_Search import compute_manhattan_distance
from Data_Point import DataPoint
from collections import defaultdict

knn_graph = defaultdict(list)
labels = dict()

print "--- Building the knn search graph ---"
m = input("Number of iterations: ")
k = input("Number of neighbors: ")
distance_metric = raw_input("Distance metric - 1. euclidean, 2. manhattan:\n")

for i in range(1, 101):
    print "Data point number: ", i
    features = [i]
    data_point = DataPoint(features=features)
    data_point.id = i
    data_point.label = i

    knn_graph = knn_data_insertion(knn_graph, distance_metric, data_point, m, k)
    print "Successful insertion of data point:", i


print "--- Searching for the K nearest neighbors from the knn search graph ---"
m = input("Number of iterations:")
k = input("Number of neighbors:")

for data_point in knn_graph.keys():
    print data_point
    neighbors = knn_search(knn_graph, distance_metric, data_point, m, k)
    neighbors = [x.id for x in neighbors]

    # actual k neighbors
    actual_neighbors = []
    for i in range(1, 101):
        # print "Test", i
        features = [i]
        point = DataPoint(features=features)
        point.id = i
        point.label = i

        if point.id != data_point.id:
            if distance_metric == "euclidean":
                actual_neighbors.append((point.id, compute_euclidean_distance(data_point, point)))
            elif distance_metric == "manhattan":
                actual_neighbors.append((point.id, compute_manhattan_distance(data_point, point)))

    actual_neighbors.sort(key=lambda x: x[1])
    k_actual_neighbors = actual_neighbors[:k]
    k_actual_neighbors = [x[0] for x in k_actual_neighbors]
    # print actual_neighbors
    print "Test point: ", data_point.id
    print "actual neighbors: ", k_actual_neighbors
    print "predicted neighbors: ", neighbors

    intersection = set(k_actual_neighbors).intersection(neighbors)
    print "Out of {} neighbors {} neighbors match".format(k, len(intersection))
