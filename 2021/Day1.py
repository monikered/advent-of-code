# How many measurements are larger than the previous measurement?

import pandas as pd
import numpy as np

with open('./2021/inputs/day1test.txt', 'r') as f:
    depths = pd.DataFrame([i.strip() for i in f.readlines()], columns=['value'])
    depths['change'] = np.NaN

# mark 'change' column as 1 if there's a row-on-row increase
def is_increasing(df):
    for i in range(1, len(df)):
        if df.loc[i, 'value'] > df.loc[i-1, 'value']:
            return 1
        else:
            return 0

# PART ONE
depths.apply(is_increasing, axis=1)
print(depths)
# answer should be 1462
print(sum(depths['change'])+1)