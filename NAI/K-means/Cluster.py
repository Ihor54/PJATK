import numpy as np


class Cluster:
    def __init__(self, name):
        self._name = name
        self._centroid = np.zeros(4)
        self._members = []

    def get_name(self):
        return self._name

    def get_centroid(self):
        return self._centroid

    def get_members(self):
        return self._members

    def remove_el(self, el):
        self._members.remove(el)

    def append_el(self, el):
        self._members.append(el)

    def __repr__(self):
        return '{} - {} - centroid {}'.format(self._name, self._members, self._centroid)

    def __str__(self):
        return '{} - {}'.format(self._name, self._members)

    def calculate_centroid(self):
        self._centroid = np.zeros(4)
        for member in self._members:
            self._centroid += member.get_specs()
        total_number = len(self._members)
        if total_number != 0:
            self._centroid /= total_number
        else:
            self._centroid = np.zeros(4)

    def calculate_frequency(self):
        total = len(self._members)
        frequency = dict.fromkeys(['Iris-virginica', 'Iris-setosa', 'Iris-versicolor'], 0)
        for m in self._members:
            frequency[m.get_name()] += 1
        return total, frequency

    def calculate_distance(self, iris_el):
        return np.sum((iris_el.get_specs() - self._centroid) ** 2)
