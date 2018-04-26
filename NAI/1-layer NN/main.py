import os
from Perceptron import *


def max_selector(perceptron_list):
    max_value = perceptron_list[0].current_output
    lang = ''
    for perceptron in perceptron_list:
        max_value = perceptron.current_output if perceptron.current_output > max_value else max_value
        lang = perceptron.name
    return lang


if __name__ == '__main__':
    os.chdir('training')
    directories = os.listdir('.')
    perceptrons = []
    alpha = 0.5
    error = 0.05
    flag = True
    for d in directories:
        perceptrons.append(Perceptron(d, alpha))
    print('Training')
    while flag:
        for d in directories:
            print(d)
            files_list = os.listdir(os.path.abspath(d))
            os.chdir(d)
            error_sum = 0
            for f in files_list:
                for p in perceptrons:
                    p.process(f)
                    error_sum += p.error
                file_language = max_selector(perceptrons)
                print('File: {}, Language: {}'.format(f, file_language))
                if error_sum >= error:
                    flag = False
            os.chdir('..')
    print('Testing')
    os.chdir('../testing')
    files_list = os.listdir('.')
    for f in files_list:
        for p in perceptrons:
            p.test(f)
        file_language = max_selector(perceptrons)
        print('File: {}, Language: {}'.format(f, file_language))

