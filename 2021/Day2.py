import pandas as pd

with open('./2021/inputs/day2.txt', 'r') as f:
    directions = f.read().strip().split("\n")


def part_one_solution(dirs=directions):

    x = y = 0

    for line in directions:
        dir, dist = line.split()
        if dir == 'down':
            y -= int(dist)
        elif dir == 'up':
            y += int(dist)
        else:
            x += int(dist)

    print(f'PART ONE: The final coordinates are a horizontal position of {x} and a depth of {abs(y)}. Their product is {x*abs(y)}.')

def part_two_solution(dirs=directions):

    x = y = z = 0
    
    for line in directions:
        dir, dist = line.split()
        if dir == 'down':
            z += int(dist)
        elif dir == 'up':
            z -= int(dist)
        else:
            x += int(dist)
            y = y + z*int(dist)

    print(f'PART TWO: The final coordinates are a horizontal position of {x} and a depth of {abs(y)}. Their product is {x*abs(y)}.')

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()