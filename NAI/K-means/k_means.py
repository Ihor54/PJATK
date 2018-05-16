import copy
import numpy as np
import os
from Cluster import Cluster
from Iris import Iris
from random import randint


# def min_distance(clstrs, iris_el):
#     min_val = np.sum((iris_el.get_specs() - clstrs[0].get_centroid()) ** 2)
#     cluster_min = clstrs[0]
#     for c in clstrs:
#         value = np.sum((iris_el.get_specs() - c.get_centroid()) ** 2)
#         if value < min_val:
#             min_val = value
#             cluster_min = c
#     return cluster_min


def iteration(clstrs, ir_data):
    # calculate centroids
    for c in clstrs:
        c.calculate_centroid()

    # assign each point to the closest cluster
    for ir_el in ir_data:
        lst = []
        for c in clstrs:
            lst.append((c, c.calculate_distance(ir_el)))
        # print(lst)
        minimum_tuple = min(lst, key=lambda x: x[1])
        # print(minimum_tuple)
        proper_cluster = minimum_tuple[0]
        if ir_el not in proper_cluster.get_members():
            for cluster in clstrs:
                if ir_el in cluster.get_members():
                    cluster.remove_el(ir_el)
            proper_cluster.append_el(ir_el)

    result = [c.get_centroid() for c in clstrs]
    return np.array(result)


if __name__ == '__main__':
    k = 2
    try:
        k = int(input('Enter the number of clusters: '))
    except ValueError:
        print('Invalid input')
    file = os.path.join(os.path.join(os.getcwd(), 'iris'), 'train.txt')
    iris_data = []
    with open(file) as f:
        for line in f:
            data = line.split(',')
            data[-1] = data[-1].replace('\n', '')
            element = Iris([float(i) for i in data[:-1]], data[-1])
            iris_data.append(element)

    clusters = []
    for i in range(k):
        clusters.append(Cluster('cluster{}'.format(i)))

    # assign random values
    for el in iris_data:
        j = randint(0, k - 1)
        clusters[j].append_el(el)
    # print(clusters)

    old_centroids = np.array([c.get_centroid() for c in clusters])
    # clusters_copy = clusters
    new_centroids = iteration(clusters, iris_data)
    i = 0
    while not np.array_equal(old_centroids, new_centroids):
        # clusters_copy = clusters
        # print('iteration{}'.format(i))
        old_centroids = copy.deepcopy(new_centroids)
        new_centroids = iteration(clusters, iris_data)
        i += 1

    total_sum, max_elements = 0, []
    purity_sum_string = ''
    for cl in clusters:
        cluster_total, species = cl.calculate_frequency()
        total_sum += cluster_total
        print('{}: {}*virginica {}*setosa {}*versicolor'.format(cl.get_name(), species['Iris-virginica'],
                                                                species['Iris-setosa'],
                                                                species['Iris-versicolor']))
        species = sorted(species.items(), key=lambda x: x[1], reverse=True)
        max_elements.append(species[0][1])
        purity_sum_string += '{}+'.format(species[0][1])
    max_elements_sum = np.sum(np.array(max_elements))
    print('Purity=({})/{}={}'.format(purity_sum_string[:-1], total_sum, max_elements_sum / total_sum))
