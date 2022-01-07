import pandas as pd

with open('./2021/inputs/day2test.txt', 'r') as f:
    directions = f.read().strip().split("\n")

x, y = 0, 0

for line in directions:
    dir, dist = line.split()
    if dir == 'down':
        y -= int(dist)
    elif dir == 'up':
        y += int(dist)
    else:
        x += int(dist)

# # # PART ONE 
print(f'The final coordinates are a horizontal position of {x} and a depth of {abs(y)}. Their product is {x*abs(y)}.')