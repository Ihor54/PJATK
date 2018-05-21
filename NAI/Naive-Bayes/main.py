from Car_class import Car
import os
from functools import reduce


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


def calculate_accuracy(known_values, predicted_values):
    i = 0
    for j in known_values:
        if j.car_class != predicted_values[1]:
            i += 1
    return i / len(known_values)


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), 'car_bayes')
    training_path = os.path.join(path, 'training')
    test_path = os.path.join(path, 'test')
    training_list = create_list_of_class_instances(training_path)
    test_list = create_list_of_class_instances(test_path)
    classes_of_cars = {car.car_class for car in training_list}
    classes_of_cars = tuple(classes_of_cars)
    car_class_probabilities = {}
    for car_class in classes_of_cars:
        counter = 0
        for c in training_list:
            if car_class == c.car_class:
                counter += 1
        probability = (counter + 1) / (len(training_list) + len(classes_of_cars))
        # print('{}, counter = {}, probability = {} '.format(car_class, counter, probability))
        car_class_probabilities[car_class] = probability
    # print(car_class_probabilities)
    test_results = []
    for el in test_list:
        x_values = el.attributes
        likelihoods = []
        for k, v in car_class_probabilities.items():
            result = (calculate_probability(x=x_values, y=k, training_set=training_list, p_y=v), k)
            likelihoods.append(result)
        likelihoods = sorted(likelihoods, key=lambda x: x[0], reverse=True)
        print('{} --------------- {}'.format(el.car_class, likelihoods[0][1]))
        test_results.append(likelihoods[0])
    accuracy = calculate_accuracy(test_list, test_results)
    print('Accuracy = {}%'.format(accuracy * 100))
