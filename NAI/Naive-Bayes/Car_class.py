class Car:
    def __init__(self, list_values):
        self.attributes = list_values[:-1]
        self.car_class = list_values[6]

    def __repr__(self):
        return '{} --- {}'.format(self.attributes, self.car_class)

    def __str__(self):
        return '{} --- {}'.format(self.attributes, self.car_class)
