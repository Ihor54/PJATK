import os
import numpy as np
from random import random, uniform
from math import exp, sqrt


class Perceptron:

    def __init__(self, name, learning_parameter):
        self.name = name
        self.learning_parameter = learning_parameter
        self.letters = dict.fromkeys(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z'], 0)
        self.weigths = np.array([uniform(0, 1) for _ in range(26)])
        # self.theta = random()
        self.error = 0
        self.current_output = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def file_freq(self, file):
        self.letters = dict.fromkeys(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z'], 0)
        size = 0
        # print(self.letters)
        with open(file, 'r') as f:
            for line in f:
                line = list(line)
                for char in line:
                    char = char.lower()
                    if char in self.letters:
                        self.letters[char] += 1
                        size += 1
        for k in self.letters:
            self.letters[k] /= size
        # return self.letters, size

    def update_weights(self, dir_name):
        # x = self.letters.values()
        # normalization = 0
        # for weight in self.weigths:
        #     normalization += weight ** 2
        # for i in range(len(self.weigths)):
        #     self.weigths[i] += self.learning_parameter * (d - y) * y * (1 - y) * x[i]
        #     self.weigths[i] /= normalization

        d = 1 if dir_name == self.name else 0
        x = np.array(list(self.letters.values()))
        # y = self.calc_activation_function()
        y = self.current_output
        normalization = np.sum(self.weigths ** 2)
        normalization = sqrt(normalization)
        self.weigths += self.learning_parameter * (d - y) * y * (1 - y) * x
        # self.weigths /= normalization
        # self.theta -= self.learning_parameter * (d - y) * y * (1 - y)
        self.calc_error(d, y)

    def calc_error(self, d, y):
        self.error = 0.5 * (d - y) ** 2

    def calc_activation_function(self):
        # dot_product = 0
        # for k, w_i in zip(self.letters, self.weigths):
        #     dot_product += self.letters[k] * w_i

        self.current_output = 0
        x = np.array(list(self.letters.values()))
        dot_product = np.sum(x * self.weigths)
        # net_value = dot_product - self.theta
        net_value = dot_product
        y = 1 / (1 + exp(-net_value))
        self.current_output = y
        # return y

    def process(self, file):
        self.file_freq(file)
        self.calc_activation_function()
        cur_dir = os.path.split(os.path.split(os.path.abspath(file))[0])[1]
        self.update_weights(cur_dir)

    def test(self, file):
        self.file_freq(file)
        self.calc_activation_function()


if __name__ == '__main__':
    pass
