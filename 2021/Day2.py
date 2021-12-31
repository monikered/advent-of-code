import pandas as pd

with open('./2021/inputs/day2test.txt', 'r') as f:
    directions = f.read().strip().split("\n")

print(directions)

# set origin
x, y = 0, 0

# replace "forward" with "x +="; "up" with "y +="; "down" with "-="
sub_key = {'forward' : 'x +=', 'up' : 'y+=', 'down' : 'y-='}

# decoded_directions = []
# for line in directions:
#     decoded_directions.append(sub_key.get(line, line))
# run each line of new input
# directions_decoded = "\n".join(sub_key.get(ele, ele) for ele in directions)
for code, math in sub_key.items():
    directions = [direction.replace(code, math) for direction in directions]

for line in directions:
    pd.eval(line)

# execute the decoded directions

# # PART ONE 
print(f'The final coordinates are a horizontal position of {x} and a depth of {abs(y)}. Their product is {x*abs(y)}.')