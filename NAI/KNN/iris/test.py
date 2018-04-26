# test_path = 'test.txt'
# result = []
# real_vals = []
# with open(test_path, 'r') as f:
#     for line in f:
#         data = line.split(',')
#         values = [float(i) for i in data[:-1]]
#         print('Values: {} - {}'.format(values, data[-1][:-1]))

neighbours = []
d = []
training_path = 'train.txt'
with open(training_path, 'r') as f:
    for line in f:
        data = line.split(',')
        # append list of values about the iris to the list neighbours
        d.append(data[-1][:-1])
        neighbours.append([float(i) for i in data[:-1]])
for i in range(0, len(neighbours)):
    print('{}. Values: {} - {}'.format(i, neighbours[i], d[i]))
