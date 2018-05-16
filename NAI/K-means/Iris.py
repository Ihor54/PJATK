import numpy as np


class Iris:
    def __init__(self, specs, name):
        self._specs = np.array(specs)
        self._name = name

    def get_name(self):
        return self._name

    def get_specs(self):
        return self._specs

    def __repr__(self):
        return '{} - {}'.format(self._specs, self._name)

    def __str__(self):
        return '{} - {}'.format(self._specs, self._name)
