from random import random


class Iris:
    def __init__(self, specs, name):
        self.specs = specs
        self.name = name
        if self.name == 'Iris-virginica':
            self.d = 1
        elif self.name == 'Iris-versicolor':
            self.d = 0
        # self.d = [1 if self.name == 'Iris-virginica' else 0]


def update_weights_and_theta(d, y, alpha, iris_el, weights_old, theta):
    """
    Updates weights and threshold
    :param d: desired output
    :param y: actual output
    :param alpha: learning parameter
    :param iris_el: element of the class Iris
    :param weights_old: list of weights
    :param theta: threshold
    """
    delta = (d - y)
    n = len(weights_old)
    for j in range(n):
        weights_old[j] += delta * alpha * iris_el.specs[j]
    # theta -= delta * alpha
    thrs = theta - delta * alpha
    return thrs


def calc_output(weights_set, iris_el, theta):
    """
    Calculates output of the perceptron
    :param weights_set: list of weights
    :param iris_el: element of the class Iris
    :param theta: threshold
    :return: output 1 or 0
    """
    dot_product = 0
    n = len(weights_set)
    for j in range(n):
        dot_product += weights_set[j] * iris_el.specs[j]
    if dot_product >= theta:
        return 1
    else:
        return 0


def update_and_calc_output(alpha, input_set, weights_old, theta, num_of_iterations):
    """
    Calculates output and updates weights provided number of iterations
    :param alpha: learning parameter
    :param input_set: training list of elements of the class Iris
    :param weights_old: list of weights
    :param theta: threshold
    :param num_of_iterations: number of the iterations
    """
    # d = 0
    for _ in range(num_of_iterations):
        for iris in input_set:
            d = iris.d
            y = calc_output(weights_old, iris, theta)
            theta = update_weights_and_theta(d, y, alpha, iris, weights_old, theta)
    return theta


def calc_accuracy(output_set, tst_set):
    """
    Calculates accuracy of the predicted Iris type
    :param output_set: set of predicted values
    :param tst_set: test set
    :return: percentage of accuracy
    """
    n = len(output_set)
    correct = 0
    for j in range(n):
        otp_name = output_set[j]
        tst_name = tst_set[j].name
        if output_set[j] == tst_set[j].name:
            correct += 1
    return correct / n * 100


def create_class_instance(line):
    """
    Splits a line a creates instance of the class Iris
    :param line: string in format pl,pw,sl,sw,type
    :return: instance of the class Iris
    """
    iris_values = line.split(',')
    iris_values[-1] = iris_values[-1].replace('\n', '')
    el = Iris([float(j) for j in iris_values[:4]], iris_values[-1])
    return el


def open_file(file):
    lst = []
    with open(file) as f:
        for line in f:
            el = create_class_instance(line)
            lst.append(el)
    return lst


def user_input():
    alpha = float(input('Provide a learning parameter: '))
    iter_num = int(input('Provide a number of iterations: '))
    switch = int(input('Do you want enter your own input or check the test set? \n'
                       '1 - test set\n'
                       '2 - own input\n'
                       'Your answer: '))
    return alpha, iter_num, switch


if __name__ == "__main__":
    desired_output = {0: 'Iris-versicolor',
                      1: 'Iris-virginica'}
    weights = [random() for _ in range(4)]
    iterations_number = 2
    learning_param = 0.2
    threshold = random()
    flag = 1
    training_set, test_set = [], []
    result = []
    try:
        training_set = open_file('iris_perceptron\\training.txt')
        learning_param, iterations_number, flag = user_input()
    except FileNotFoundError:
        print('File is no found')
    except ValueError:
        print('Invalid input')
    # print('weights before updating: {} \n threshold : {}'.format(weights, threshold))
    threshold = update_and_calc_output(learning_param, training_set, weights, threshold, iterations_number)
    if flag == 1:
        try:
            test_set = open_file('iris_perceptron\\test.txt')
        except FileNotFoundError:
            print('File is no found')
        new_set = []
        for i in range(len(test_set)):
            new_set.append(test_set[i])
            result.append(desired_output[calc_output(weights, test_set[i], threshold)])
            print('Predicted: {} ---- Real: {}'.format(result[i], test_set[i].name))
        accuracy = calc_accuracy(result, test_set)
        print('Accuracy: {}'.format(accuracy))
    elif flag == 2:
        user_example = []
        try:
            user_example = input('Enter your example according to format - pl,pw,sl,sw,species\n'
                                 'Your input: ')
        except Exception:
            print('Invalid input')
        test_set.append(create_class_instance(user_example))
        result.append(desired_output[calc_output(weights, test_set[0], threshold)])
        print('Predicted: {} ---- Real: {}'.format(result[0], test_set[0].name))
        accuracy = calc_accuracy(result, test_set)
        print('Accuracy: {}'.format(accuracy))
    # print('weights after updating: {} \n threshold : {}'.format(weights, threshold))
