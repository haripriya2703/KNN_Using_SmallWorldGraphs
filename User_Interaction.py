from Data_Insertion import knn_data_insertion
from KNN_Classifier import knn_classifier
from Data_Point import DataPoint


knn_graph = []
m = input("Number of iterations:")
k = input("Number of neighbors:")
while True:
    print "Input the features of your data point"
    petal_length = input("Petal length:")
    petal_width = input("Petal Width:")
    sepal_length = input("Sepal Length:")
    sepal_width = input("Sepal Width:")
    data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)

    choice = input("1-Insert and Classify, 2-Classify")
    if choice == 1:
        data_point.id = len(knn_graph) + 1
        knn_graph = knn_data_insertion(knn_graph, data_point, m, k)
    data_point.label = knn_classifier(knn_graph, data_point, m, k)
    print "Label of data point: ", data_point.label

    more_data = input("Do you want to input more data? Y/N")
    if more_data == 'N' or more_data == 'n':
        break
