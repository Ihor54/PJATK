import numpy
import pylab
import random
import os
import datetime


class GameOfLife:

    def __init__(self, N=100, T=200, flag=2):
        """ Set up Conway's Game of Life. """
        # Here we create two grids to hold the old and new configurations.
        # This assumes an N*N grid of points.
        # Each point is either alive or dead, represented by integer values of 1 and 0, respectively.
        self.config = []
        self.N = N
        self.old_grid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.new_grid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.T = T  # The maximum number of generations

        if flag == 1:
            with open('config.txt', 'r') as f:
                for line in f:
                    line = line.split(',')
                    self.config.append((int(line[1]), int(line[0])))
            for i in range(0, self.N):
                for j in range(0, self.N):
                    coord = (i, j)
                    if coord in self.config:
                        self.old_grid[i][j] = 1
                    else:
                        self.old_grid[i][j] = 0

        if flag == 2:
            # Set up a random initial configuration for the grid.
            for i in range(0, self.N):
                for j in range(0, self.N):
                    if random.randint(0, 100) < 15:
                        self.old_grid[i][j] = 1
                    else:
                        self.old_grid[i][j] = 0

    def live_neighbours(self, i, j):
        """ Count the number of live neighbours around point (i, j). """
        s = 0  # The total number of live neighbours.
        # Loop over all the neighbours.
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if x == i and y == j:
                    continue  # Skip the current point itself - we only want to count the neighbours!
                if x != self.N and y != self.N:
                    s += self.old_grid[x][y]
                # The remaining branches handle the case where the neighbour is off the end of the grid.
                # In this case, we loop back round such that the grid becomes a "toroidal array".
                elif x == self.N and y != self.N:
                    s += self.old_grid[0][y]
                elif x != self.N and y == self.N:
                    s += self.old_grid[x][0]
                else:
                    s += self.old_grid[0][0]
        return s

    def play(self, survive1, survive2, alive):
        """ Play Conway's Game of Life. """

        now = datetime.datetime.now()
        new_dir = os.path.join(os.getcwd(), 'Game of life {}'.format(now.strftime("%Y-%m-%d %H%M")))
        os.mkdir(new_dir)
        os.chdir(new_dir)
        # Write the initial configuration to file.
        pylab.pcolormesh(self.old_grid)
        pylab.colorbar()
        pylab.savefig("generation0.png")

        t = 1  # Current time level
        write_frequency = 1  # How frequently we want to output a grid configuration.
        while t <= self.T:  # Evolve!
            print("At time level {}".format(t))

            # Loop over each cell of the grid and apply Conway's rules.
            for i in range(self.N):
                for j in range(self.N):
                    live = self.live_neighbours(i, j)
                    if self.old_grid[i][j] == 1 and live < survive1:
                        self.new_grid[i][j] = 0  # Dead from starvation.
                    elif self.old_grid[i][j] == 1 and (live == survive1 or live == survive2):
                        self.new_grid[i][j] = 1  # Continue living.
                    elif self.old_grid[i][j] == 1 and live > alive:
                        self.new_grid[i][j] = 0  # Dead from overcrowding.
                    elif self.old_grid[i][j] == 0 and live == alive:
                        self.new_grid[i][j] = 1  # Alive from reproduction.

            # Output the new configuration.

            if t % write_frequency == 0:
                pylab.pcolormesh(self.new_grid)
                pylab.savefig("generation{}.png".format(t))

            # The new configuration becomes the old configuration for the next generation.
            self.old_grid = self.new_grid.copy()

            # Move on to the next time level
            t += 1

        os.chdir('..')


if __name__ == "__main__":
    rules = {'survive1': 0,
             'survive2': 0,
             'alive': 0}
    user_rules = input('Please enter your own rules in such format s1,s2,a: ')
    size_of_grid = int(input('Please provide size of the grid: '))
    num_of_generations = int(input('Please provide number of the generations: '))
    is_random_config = int(input('Do you want to provide your own configuration or generate randomly?\n'
                                 '1 - your own \n'
                                 '2 - generate randomly\n'
                                 'Your answer : '))
    user_rules = user_rules.split(',')
    rules['survive1'] = int(user_rules[0])
    rules['survive2'] = int(user_rules[1])
    rules['alive'] = int(user_rules[2])
    game = GameOfLife(size_of_grid, num_of_generations, is_random_config)
    game.play(rules['survive1'], rules['survive2'], rules['alive'])
