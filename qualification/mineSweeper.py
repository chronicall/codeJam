#!/usr/bin/env python2.7

from sys import argv
import random

script, filename = argv

inp = open(filename)

cases = int(inp.readline())
for num in range(0, cases):
    line = inp.readline()
    line = line.rstrip('\n').split(' ')
    line = [int(x) for x in line]
    R, C, M = line
    #print 'R: %d --- C: %d --- M: %d' % (R, C, M)
    grid = []
    for i in range(0, R):
        grid.append([])
        for j in range(0, C):
            grid[i].append('.')
    m = M
    while m > 0:
        x = random.randint(0, R - 1)
        y = random.randint(0, C - 1)
        #print '' % (x, y)
        if grid[x][y] == '.':
            grid[x][y] = '*'
            m = m - 1
    
    for i in range(0, R):
        for j in range(0, C):
            print grid[i][j],
        print ' '
