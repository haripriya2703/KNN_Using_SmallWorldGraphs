from Data_Insertion_Objs import knn_data_insertion
from KNN_Search import knn_search
from KNN_Search import compute_euclidean_distance
from KNN_Search import compute_manhattan_distance
from Data_Point import DataPoint
from collections import defaultdict

import csv
import random


knn_graph = defaultdict(list)
labels = dict()
csv_list = []

# User input parameters
print "--- Building the knn search graph ---"
m = input("Number of iterations: ")
k = input("Number of neighbors: ")
distance_metric = raw_input("Distance metric - 1. euclidean, 2. manhattan:\n")

with open('IRIS.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    csv_list = list(readCSV)
    n = len(csv_list)
    random.shuffle(csv_list)
    print "Length of the given data is: ", n

    for i, row in enumerate(csv_list):
        # print "Data point number: ", i
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        features = [petal_length, petal_width, sepal_length, sepal_width]

        # create a new data point
        data_point = DataPoint(features=features)
        data_point.id = i + 1
        data_point.label = row[4]

        knn_graph = knn_data_insertion(knn_graph, distance_metric, data_point, m, k)

print "--- Searching for the K nearest neighbors from the knn search graph ---"
m = input("Number of iterations: ")
k = input("Number of neighbors: ")

for data_point in knn_graph.keys():
    neighbors = knn_search(knn_graph, distance_metric, data_point, m, k)
    neighbors = [x.id for x in neighbors]

    # actual k neighbors
    actual_neighbors = []
    for i, row in enumerate(csv_list):
        print "Test", i
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        features = [petal_length, petal_width, sepal_length, sepal_width]

        # create a new data point
        point = DataPoint(features=features)
        point.id = i + 1
        point.label = row[4]

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
    print len(intersection)
