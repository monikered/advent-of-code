# How many measurements are larger than the previous measurement?

from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

with open('./2021/inputs/day1.txt', 'r') as f:
    depths = pd.DataFrame([int(i) for i in f.readlines()], columns=['value'])
    depths['change'] = np.NaN

for i in range(len(depths)):
    if i == 0:
        pass
    elif depths.iloc[i, 0] > depths.iloc[i-1, 0]:
        depths.iloc[i, 1] = 1
    else:
        depths.iloc[i, 1] = 0
# # PART ONE
# depths.apply(is_increasing, axis=1)
print(depths)
# # answer should be 1462
print('The answer is '+ str(np.sum(depths['change'])))