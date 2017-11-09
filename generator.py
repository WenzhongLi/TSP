#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import random
import sys


class Generator(object):
    # init size and density of map
    def __init__(self, size, max_length):
        self.size = size
        self.max_length = max_length
        self.map_matrix = []
        for k in range(self.size):
            self.map_matrix.append([])
            for j in range(self.size):
                self.map_matrix[k].append(0)

    # print map to commend line
    def print_matrix(self):
        count_blocked = 0
        for k in range(self.size + 1):
            for j in range(self.size + 1):
                if k == 0 and j == 0:
                    print "  ",
                    continue
                elif k == 0:
                    if j > 10:
                        print str(j - 1),
                    else:
                        print " " + str(j - 1),
                    continue
                elif j == 0:
                    if k > 10:
                        print str(k - 1),
                    else:
                        print " " + str(k - 1),
                    continue
                if self.map_matrix[k-1][j-1] < 10:
                    print " "+str(self.map_matrix[k-1][j-1]),
                elif self.map_matrix[k-1][j-1] < 100:
                    print self.map_matrix[k-1][j-1],
                else:
                    print(self.map_matrix[k-1][j-1]),
            print('\n'),

    # paint maze randomly
    def paint_random(self):
        matrix = [[0 for j in range(self.size)] for k in range(self.size)]
        node_list = []
        # init a set of all point could be block
        for k in range(self.size):
            for j in range(self.size):
                matrix[k][j] = random.choice(range(1,self.max_length))
        for k in range(self.size):
            for j in range(self.size):
                matrix[k][j] = matrix[j][k]
                if k == j:
                    matrix[k][j] = 0
        self.map_matrix = matrix
        return matrix

    def get_matrix(self):
        return self.map_matrix

    def extend_matrix(self):
        self.size += 1
        matrix = [[0 for j in range(self.size)] for k in range(self.size)]
        for k in range(self.size - 1):
            for j in range(self.size - 1):
                matrix[k][j] = self.map_matrix[k][j]
        for k in range(self.size - 1):
            matrix[k][self.size - 1] = random.choice(range(self.max_length))
            matrix[self.size - 1][k] = random.choice(range(self.max_length))
        self.map_matrix = matrix
        return matrix


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    # set the size and density of this matrix
    generator = Generator(10, 100)
    generator.print_matrix()
    generator.paint_random()
    generator.print_matrix()
    generator.extend_matrix()
    generator.print_matrix()
    print ('start over')