#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:59:11 2020

@author: monicaremmers
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:00:29 2020

@author: monicaremmers
"""

right_list = [1, 3, 5, 7, 1]
down_list = [1, 1, 1, 1, 2]

def part1(inputmap, right, down):
    x = right
    y = down
    trees = 0
    while y < len(inputmap):
        if x > len(inputmap[y]) - 1:
            x = x % len(inputmap[y])
        if inputmap[y][x] == '#':
            trees += 1
        x += right
        y += down
    return trees



if __name__ == "__main__":
    inputmap = [line.rstrip() for line in open('./inputs/day3.txt', 'r')]
    print('Part 1: ', part1(inputmap, 3, 1))
    tree_product = 1
    for (right, down) in zip(right_list, down_list):
        tree_product *= part1(inputmap, right, down)
    print('Part 2: ',tree_product)
