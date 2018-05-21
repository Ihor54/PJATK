from Car_class import Car
import os


def create_list_of_class_instances(file):
    instances_list = []
    with open(file) as f:
        for line in f:
            data = line.split(',')
            data[-1] = data[-1].replace('\n', '')
            class_element = Car([i for i in data])
            instances_list.append(class_element)
    return instances_list


def calculate_probability(x, y, training):
    x_len = len(x)
    data = [i for i in training if i.car_class == y]
    lists = []
    for i in range(x_len):
        lists.append([j for j in data if j.attributes[i] == x[i]])
    lists_1 = [[j for j in data if j.attributes[i] == x[i]] for i in range(x_len)]
    print(lists == lists_1)
    # # p1 = (lists[0] + 1) / (len(data) + len(set(lists[0])))
    # price = [i for i in data if i.attributes[0] == x[0]]
    # maintenance = [i for i in data if i.attributes[1] == x[1]]
    # doors = [i for i in data if i.attributes[2] == x[2]]
    # capacity = [i for i in data if i.attributes[3] == x[3]]
    # luggage = [i for i in data if i.attributes[4] == x[4]]
    # safety = [i for i in data if i.attributes[5] == x[5]]
    # lists = [price, maintenance, doors, capacity, luggage, safety]
    # p = []
    # for i in range(len(x)):
    #     p1 = (len(lists[i]) + 1) / (len(data) + len({j.attributes[i] for j in data}))
    #     p.append(p1)

    return lists


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
        # unique_values = {car.car_class for car in training_list}
        probability = (counter + 1) / (len(training_list) + len(classes_of_cars))
        print('{}, counter = {}, probability = {} '.format(car_class, counter, probability))
        car_class_probabilities[car_class] = probability
    print(car_class_probabilities)
    print(calculate_probability(test_list[0].attributes, 'acc', training_list))
    # for el in test_list:
    #     x_values = el.attributes


# print(training_path)
# print(test_path)
# print(training_list)
# print(test_list)
# print(classes_of_cars)
