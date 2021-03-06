#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:53:51 2020

@author: monicaremmers
"""

from itertools import permutations
print('Please enter list of numbers.')
numbers = [ int(x) for x in input().split()]
part_one_solutions = [pair for pair in permutations(numbers, 2) if sum(pair) == 2020]
part_two_solutions = [trip for trip in permutations(numbers, 3) if sum(trip) == 2020]
print('Part One. The matching pair is {} and their product is {}.'.format(part_one_solutions[0],part_one_solutions[0][0]*part_one_solutions[0][1]))
print('Part Two. The matching three numbers are {} and their product is {}.'.format(part_two_solutions[0],part_two_solutions[0][0]*part_two_solutions[0][1]*part_two_solutions[0][2]))