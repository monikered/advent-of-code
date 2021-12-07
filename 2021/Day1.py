# How many measurements are larger than the previous measurement?
import pandas as pd

with open('./2021/inputs/day1.txt', 'r') as f:
    depths = pd.DataFrame([i.strip() for i in f.readlines()], columns=['value'])
    depths['change'] = 0

# mark 'change' column as 1 if there's a row-on-row increase
for i in range(1, len(depths)):
    if depths.loc[i, 'value'] > depths.loc[i-1, 'value']:
        depths.loc[i, 'change'] = 1
    else:
        depths.loc[i, 'change'] = 0

print(sum(depths['change']))