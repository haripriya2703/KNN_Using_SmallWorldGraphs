class DataPoint(object):
    def __init__(self, features=[], id=None, distance=None, label=None):
        self.id = id
        self.features = features
        self.dist = distance
        self.label = label
