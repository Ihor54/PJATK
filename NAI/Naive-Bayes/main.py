from Car_class import Car
import os
from functools import reduce

path = os.path.join(os.getcwd(), 'car_bayes')
training_path = os.path.join(path, 'training')
test_path = os.path.join(path, 'test')


def create_list_of_class_instances(file):
    instances_list = []
    with open(file) as f:
        for line in f:
            data = line.split(',')
            data[-1] = data[-1].replace('\n', '')
            class_element = Car([i for i in data])
            instances_list.append(class_element)
    return instances_list


def calculate_probability(x, y, training_set, p_y):
    x_len = len(x)
    data = [i for i in training_set if i.car_class == y]
    lists = [[j for j in data if j.attributes[i] == x[i]] for i in range(x_len)]
    p = [p_y]
    for i in range(x_len):
        unique_attributes = {j.attributes[i] for j in data}
        p1 = (len(lists[i]) + 1) / (len(data) + len(unique_attributes))
        p.append(p1)
    likelihood = reduce(lambda i, j: i * j, p)
    return likelihood


def predict_value_for_test_example(class_probabilities, test_example):
    x_values = test_example.attributes
    likelihoods = []
    for k, v in class_probabilities.items():
        probability_of_item = (calculate_probability(x=x_values, y=k, training_set=training_list, p_y=v), k)
        likelihoods.append(probability_of_item)
    likelihoods = sorted(likelihoods, key=lambda x: x[0], reverse=True)
    best_likelihood = likelihoods[0]
    return best_likelihood


def calculate_accuracy(known_values, predicted_values):
    i = 0
    for j in known_values:
        if j.car_class != predicted_values[1]:
            i += 1
    return i / len(known_values)


if __name__ == '__main__':
    flag = 0
    user_example = ''
    try:
        flag = int(input('Do you want to test examples from a test file or provide your own example? \n'
                         '0 - test examples from a test file \n'
                         '1 - provide your own example\n'
                         'Your answer: '))
        if flag == 1:
            user_example = input('Provide your example: ')
    except ValueError:
        print('Invalid input')

    # create list of instances of class Car from test and training files
    training_list = create_list_of_class_instances(training_path)
    test_list = create_list_of_class_instances(test_path)

    # create a set of all unique classes of cars
    classes_of_cars = tuple({car.car_class for car in training_list})
    # classes_of_cars = tuple(classes_of_cars)

    # for each class calculate its probability
    car_class_probabilities = {}
    for car_class in classes_of_cars:
        counter = 0
        # for each class count number of elements in the training list with the same class_name
        for c in training_list:
            if car_class == c.car_class:
                counter += 1
        # compute the probability with smoothing
        probability = (counter + 1) / (len(training_list) + len(classes_of_cars))
        # add current class and its probability to the dictionary
        car_class_probabilities[car_class] = probability

    if flag == 0:
        # predict the value for each test example
        test_results = []
        for el in test_list:
            result = predict_value_for_test_example(car_class_probabilities, el)
            print('Labelled: {} --------------- predicted: {}'.format(el.car_class, result[1]))
            test_results.append(result)
        accuracy = calculate_accuracy(test_list, test_results)
        print('Accuracy = {}%'.format(accuracy * 100))

    elif flag == 1:
        # predict the value for user_example
        user_example = user_example.split(',')
        user_example[-1] = user_example[-1].replace('\n', '')
        user_example = Car([i for i in user_example])
        result = predict_value_for_test_example(car_class_probabilities, user_example)
        print('Labelled: {} --------------- predicted: {}'.format(user_example.car_class, result[1]))
