from Data_Insertion_Objs import knn_data_insertion
from KNN_Search import knn_search
from KNN_Search import compute_euclidean_distance
from KNN_Search import compute_manhattan_distance
from Data_Point import DataPoint
from collections import defaultdict
from Queue import PriorityQueue
import csv
import random
import numpy as np

knn_graph = defaultdict(list)
labels = dict()
m = input("Number of iterations:")
k = input("Number of neighbors:")

for i in range(1, 101):
    print "Data point number: ", i
    petal_length = i
    data_point = DataPoint(petal_length)
    data_point.id = i
    data_point.label = i

    knn_graph = knn_data_insertion(knn_graph, data_point, m, k)
    print "Successful insertion of data point:", i

m = input("Number of iterations:")
k = input("Number of neighbors:")

for data_point in knn_graph.keys():
    print data_point
    neighbors = knn_search(knn_graph, data_point, m, k)
    neighbors = [x.id for x in neighbors]

    # actual k neighbors
    actual_neighbors = []
    for i in range(1, 101):
        # print "Test", i
        petal_length = i
        point = DataPoint(petal_length)
        point.id = i
        point.label = i

        if point.id != data_point.id:
            actual_neighbors.append((point.id, compute_manhattan_distance(data_point, point)))

    actual_neighbors.sort(key=lambda x: x[1])
    k_actual_neighbors = actual_neighbors[:k]
    k_actual_neighbors = [x[0] for x in k_actual_neighbors]
    print actual_neighbors
    print "Test point: ", data_point.id
    print "actual neighbors: ", k_actual_neighbors
    print "predicted neighbors: ", neighbors

    intersection = set(actual_neighbors).intersection(neighbors)
    print len(intersection)
