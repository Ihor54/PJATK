class Car:
    def __init__(self, list_values):
        # self.price = list_values[0]
        # self.maintenance = list_values[1]
        # self.doors = list_values[2]
        # self.capacity = list_values[3]
        # self.luggage = list_values[4]
        # self.safety = list_values[5]
        self.attributes = list_values[:-1]
        self.car_class = list_values[6]

    def __repr__(self):
        return '{} --- {}'.format(self.attributes, self.car_class)

    def __str__(self):
        return '{} --- {}'.format(self.attributes, self.car_class)
