class DataPoint(object):
    def __init__(self, petal_length=-1, petal_width=-1, sepal_length=-1, sepal_width=-1, label=None, neighbors=[],
                 id=None):
        # self.petal_length = petal_length
        # self.petal_width = petal_width
        # self.sepal_length = sepal_length
        # self.sepal_width = sepal_width
        # or
        self.id = id
        self.features = [petal_length, petal_width, sepal_length, sepal_width]
        self.label = label
        self.neighbors = neighbors

