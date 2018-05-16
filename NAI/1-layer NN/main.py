import os
from Perceptron import *


def max_selector(perceptron_list):
    max_value = perceptron_list[0].current_output
    lang = perceptron_list[0].name
    for perceptron in perceptron_list:
        if perceptron.current_output > max_value:
            max_value = perceptron.current_output
            lang = perceptron.name
    return lang


if __name__ == '__main__':
    os.chdir('training')
    directories = os.listdir('.')
    perceptrons = []
    alpha = 0.5
    error = 3
    flag = True
    for d in directories:
        perceptrons.append(Perceptron(d, alpha))
    print('================================== Training ==================================')
    while flag:
        # for i in range(10):
        #     print('iteration {}'.format(i))
        for d in reversed(directories):
            # print(d)
            files_list = os.listdir(os.path.abspath(d))
            os.chdir(d)
            error_sum = 0
            for f in files_list:
                # print('Directory {} File {}'.format(d, f))
                for p in perceptrons:
                    p.process(f)
                    # print('Perceptron {} - output {}'.format(p.name, p.current_output))
                    error_sum += p.error
                file_language = max_selector(perceptrons)
                # print('Language: {}\n'.format(file_language))

            os.chdir('..')
            if error_sum < error:
                flag = False
            print('Error {}'.format(error_sum))
    print('================================== Testing ==================================')
    os.chdir('../testing')
    files_list = os.listdir('.')
    for f in files_list:
        print('File {}'.format(f))
        for p in perceptrons:
            p.test(f)
            print('Perceptron {} - output {}'.format(p.name, p.current_output))
        file_language = max_selector(perceptrons)
        print('File: {}, Language: {}'.format(f, file_language))
