from Data_Insertion import knn_data_insertion
from KNN_Classifier import knn_classifier
from Data_Point import DataPoint


knn_graph = []
while True:
    print "Input the features of your data point"
    petal_length = input("Petal length?")
    petal_width = input("Petal Width?")
    sepal_length = input("Sepal Length?")
    sepal_width = input("Sepal Width?")
    data_point = DataPoint(petal_length, petal_width, sepal_length, sepal_width)
    m = 2
    k = 7
    while True:
        choice = input("1-Insert and Classify, 2-Classify")
        if choice == 1:
            knn_graph = knn_data_insertion(knn_graph, data_point, m, k)
            print "Label of data point: ", knn_classifier(knn_graph, data_point, m, k)
            break
        elif choice == 2:
            print "Label of data point: ", knn_classifier(knn_graph, data_point, m, k)
            break
        else:
            print "Incorrect choice"

    more_data = input("Do you want to input more data? Y/N")
    if more_data == 'N' or more_data == 'n':
        break
