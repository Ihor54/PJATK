from math import sqrt
from operator import itemgetter


def predict_val(input_line, nbours, tr_names, number_k):
    """
    predicts the type of the flower based on its parameters
    :param input_line: the string line of format pl,pw,sl,sw,type of the test item
    :param nbours: list of training set values
    :param tr_names: list of training set types
    :param number_k: number of neighbours to compare with
    :return: predicted type of the flower
    """
    d = input_line.split(',')
    values = [float(v) for v in d[0:-1]]
    if d[-1][-1] == '\n':
        real_species = d[-1][:-1]
    else:
        real_species = d[-1]
    # calculate distances of items from training set to item from test set
    distances = [calc_distance(i, values) for i in nbours]
    # sort neighbours in ascending order
    spec_dist = list(zip(tr_names, distances))
    spec_dist = sorted(spec_dist, key=itemgetter(1))
    return best_neighbour(spec_dist, number_k), real_species


def best_neighbour(nb_distance, num_k):
    """
    takes the list of distances between test item and all items from the training set and returns the predicted type of the flower
    :param nb_distance: list of distances
    :param num_k: number of neighbours to compare with
    :return: predicted the best type of Iris for the input data
    """
    species = {
        'Iris-virginica': [],
        'Iris-versicolor': [],
        'Iris-setosa': []
    }
    # take k neighbours with smallest distance
    kNN = nb_distance[:num_k]
    for item in kNN:
        species[item[0]].append(item[1])
    # choose the majority of neighbours
    majority = sorted(species.items(), key=lambda it: len(it[1]), reverse=True)
    # if there is equal number of neighbours in first two lists of majority - we take one with smaller average distance
    if len(majority[0][0]) == len(majority[1][0]) and len(majority[0][0]) != 0:
        dist = {majority[0][0]: average_distance(majority[0][1]),
                majority[1][0]: average_distance(majority[1][1])}
        best_nb = sorted(dist.items(), key=lambda x: x[1])
        return best_nb[0][0]
    # if there is equal number of neighbours in all lists of majority - we take one with smaller average distance
    if len(majority[0][0]) == len(majority[2][0]) and len(majority[0][0]) != 0:
        dist = {majority[0][0]: average_distance(majority[0][1]),
                majority[1][0]: average_distance(majority[1][1]),
                majority[2][0]: average_distance(majority[2][1])}
        best_nb = sorted(dist.items(), key=lambda x: x[1])
        return best_nb[0][0]
    else:
        return majority[0][0]


def average_distance(lst_distances):
    """
    takes the list of distances and returns the average value
    :param lst_distances: list of distances
    :return: the average value
    """
    sum = 0
    for i in lst_distances:
        sum += i
    return sum / len(lst_distances)


def calc_distance(train, test):
    """
    takes the
    :param train: list of 4 numbers of the training item
    :param test: list of 4 numbers of the test item
    :return: the Euclidean distance between these items
    """
    return sqrt(
        (test[0] - train[0]) ** 2 + (test[1] - train[1]) ** 2 + (test[2] - train[2]) ** 2 + (test[3] - train[3]) ** 2)


if __name__ == '__main__':
    k = 4
    flag = 2
    user_input = ''
    try:
        k = int(input('Enter the number of nearest neighbours: '))
        flag = int(input('Do you want enter your own input or check the test set? \n'
                         '1 - own input\n'
                         '2 - test set\n'
                         'Your answer: '))
        if flag == 1:
            user_input = input('Enter your example according to format - pl,pw,sl,sw,species\n'
                               'Your input: ')
    except ValueError:
        print('Invalid input')
    neighbours, names = [], []
    # read all items from the training set
    training_path = 'iris\\train.txt'
    with open(training_path, 'r') as f:
        for line in f:
            data = line.split(',')
            # append list of values about the iris to the list neighbours
            neighbours.append([float(el) for el in data[:-1]])
            names.append(data[-1][:-1])
    result = []
    real_names = []
    if flag == 2:
        # if user enters 2 - we read all values from the test file and find their types
        test_path = 'iris\\test.txt'
        with open(test_path, 'r') as f:
            for line in f:
                new_val, rl_name = predict_val(line, neighbours, names, k)
                result.append(new_val)
                real_names.append(rl_name)
    elif flag == 1:
        # if user enters 1 - we read user's input and find its type
        new_val, rl_name = predict_val(user_input, neighbours, names, k)
        result.append(new_val)
        real_names.append(rl_name)
    wrong, num = 0, 0
    for p, r in zip(result, real_names):
        if p != r:
            wrong += 1
        num += 1
        print('Predicted: {}, Real: {}'.format(p, r))
    print('Accuracy: {}%'.format(100 - wrong / num * 100))