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
    neighbors = knn_search(knn_graph, distance_metric, data_point, m, k)
    neighbors_id = [x.id for x in neighbors]

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
                actual_neighbors.append((point, compute_euclidean_distance(data_point, point)))
            elif distance_metric == "manhattan":
                actual_neighbors.append((point, compute_manhattan_distance(data_point, point)))

    actual_neighbors.sort(key=lambda x: x[1])
    k_actual_neighbors = actual_neighbors[:k]
    # print k_actual_neighbors
    k_actual_neighbors = [x[0] for x in k_actual_neighbors]
    # print k_actual_neighbors
    k_actual_neighbors_id = [x.id for x in k_actual_neighbors]
    # print k_actual_neighbors_id
    # print actual_neighbors
    print "----------------"
    print "Test point: ", data_point.id
    print "actual neighbors: ", k_actual_neighbors_id
    print "predicted neighbors: ", neighbors_id

    intersection = set(k_actual_neighbors_id).intersection(neighbors_id)
    print "Out of {} neighbors {} neighbors match".format(k, len(intersection))
    accuracy = float(len(intersection))*100 / k
    print "Percent accuracy in terms of number of neighbors: {}%".format(accuracy)

    actual_mean_distance = 0
    predicted_mean_distance = 0
    for a, p in zip(k_actual_neighbors, neighbors):
        if distance_metric == "euclidean":
            actual_mean_distance += compute_euclidean_distance(data_point, a)
            predicted_mean_distance += compute_euclidean_distance(data_point, p)
        elif distance_metric == "manhattan":
            actual_mean_distance += compute_manhattan_distance(data_point, a)
            predicted_mean_distance += compute_manhattan_distance(data_point, p)

    actual_mean_distance = actual_mean_distance/k
    predicted_mean_distance = predicted_mean_distance/k
    print "Actual mean distance of K neighbors from Query point: "
    print actual_mean_distance
    print "Predicted mean distance of K neighbors from Query point: "
    print predicted_mean_distance
