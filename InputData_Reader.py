from Data_Insertion_Objs import knn_data_insertion
from KNN_Classifier import knn_classifier
from Data_Point import DataPoint
from collections import defaultdict
import csv

knn_graph = defaultdict(list)
labels = dict()
m = input("Number of iterations:")
k = input("Number of neighbors:")

with open('IRIS.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    for row in readCSV:
        petal_length = row[0]
        petal_width = row[1]
        sepal_length = row[2]
        sepal_width = row[3]
        data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
        data_point.id = len(knn_graph) + 1
        data_point.label = row[4]
        knn_graph = knn_data_insertion(knn_graph, data_point, m, k)
