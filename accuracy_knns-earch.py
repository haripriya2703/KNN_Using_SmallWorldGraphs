from Data_Insertion_Objs import knn_data_insertion
from KNN_Search import knn_search
from KNN_Search import compute_euclidean_distance
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
csv_list = []

with open('IRIS.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    csv_list = list(readCSV)
    n = len(csv_list)
    random.shuffle(csv_list)
    print "Length of the given data is: ", n

    for i, row in enumerate(csv_list):
        print "Data point number: ", i
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
        data_point.id = i + 1
        data_point.label = row[4]

        knn_graph = knn_data_insertion(knn_graph, data_point, m, k)


m = input("Number of iterations:")
k = input("Number of neighbors:")

for data_point in knn_graph.keys():
    neighbors = knn_search(knn_graph, data_point, m, k)
    neighbors = [x.id for x in neighbors]

    # actual k neighbors
    actual_neighbors = []
    for i, row in enumerate(csv_list):
        # print "Test", i
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
        point.id = i + 1
        point.label = row[4]

        if point != data_point:
            actual_neighbors.append((point.id, compute_euclidean_distance(data_point, point)))

    actual_neighbors.sort(key=lambda x: x[1])
    k_actual_neighbors = actual_neighbors[:k]
    k_actual_neighbors = [x[0] for x in k_actual_neighbors]
    print actual_neighbors
    print k_actual_neighbors, neighbors

    intersection = set(actual_neighbors).intersection(neighbors)
    print len(intersection)
