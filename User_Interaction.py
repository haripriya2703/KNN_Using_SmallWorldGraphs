from Data_Insertion import knn_data_insertion
from KNN_Classifier import knn_classifier
from Data_Point import DataPoint
from collections import defaultdict


knn_graph = defaultdict(list)
labels = dict()
m = input("Number of iterations:")
k = input("Number of neighbors:")
i = 1
while True:
    print "Input the features of your data point"
    petal_length = input("Petal length:")
    petal_width = input("Petal Width:")
    sepal_length = input("Sepal Length:")
    sepal_width = input("Sepal Width:")
    data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
    if i <= k:
        label = raw_input("Label of data point:")
        data_point.id = len(knn_graph) + 1
        knn_graph = knn_data_insertion(knn_graph, data_point, m, k)
        labels[data_point.id] = label
    else:
        choice = input("1-Insert and Classify, 2-Classify")
        if choice == 1:
            data_point.id = len(knn_graph) + 1
            knn_graph = knn_data_insertion(knn_graph, data_point, m, k)
        labels[data_point.id] = knn_classifier(knn_graph, data_point, m, k, labels)
        print "Label of data point: ", labels[data_point.id]

    i += 1
    more_data = raw_input("Do you want to input more data? Y/N")
    if more_data == 'N' or more_data == 'n':
        break
