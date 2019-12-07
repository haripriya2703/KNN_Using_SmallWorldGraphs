from Data_Insertion_Objs import knn_data_insertion
from KNN_Classifier import knn_classifier
from Data_Point import DataPoint
from collections import defaultdict
import csv
import random

knn_graph = defaultdict(list)
labels = dict()
m = input("Number of iterations:")
k = input("Number of neighbors:")

with open('IRIS.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    csv_list = list(readCSV)
    n = len(csv_list)
    random.shuffle(csv_list)
    print "Length of the given data is: ", n
    train_data_size = 120

    for i, row in enumerate(csv_list):
        print "Data point number: ", i
        if i == train_data_size:
            break
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
        data_point.id = i + 1
        data_point.label = row[4]

        knn_graph = knn_data_insertion(knn_graph, data_point, m, k)

    # print the graph built using the data
    for key in sorted(knn_graph.keys()):
        neighbor_obj = knn_graph[key]
        neighbors = []
        for neighbor in neighbor_obj:
            neighbors.append(neighbor.id)

        print key.id, neighbors

    species_labels = ['Iris-setosa', 'Iris-virginica', 'Iris-versicolor']
    confusion_matrix = [[0 for i in range(3)] for j in range(3)]

    for i in range(train_data_size+1, n):
        row = csv_list[i]
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
        data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
        data_point.id = i + 1
        data_point.label = row[4]

        original_label = data_point.label
        original_label_index = species_labels.index(original_label)
        predicted_label_index, predicted_label = knn_classifier(knn_graph, data_point, m, k)
        print i, original_label, predicted_label

        confusion_matrix[original_label_index][predicted_label_index] += 1

    print confusion_matrix
