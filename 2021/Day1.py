# # How many measurements are larger than the previous measurement?

from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

with open('./2021/inputs/day1test.txt', 'r') as f:
    depths = pd.DataFrame([int(i) for i in f.readlines()], columns=['value'])
    depths['change'] = np.NaN

# # # PART ONE

for i in range(len(depths)):
    if i == 0:
        pass
    elif depths.iloc[i, 0] > depths.iloc[i-1, 0]:
        depths.iloc[i, 1] = 1
    else:
        depths.iloc[i, 1] = 0

# # answer should be 1462
print('The answer is '+ str(np.sum(depths['change'])))

# # PART TWO

triplets = pd.DataFrame([depths.iloc[int(i):int(i)+3, 0] for i in range(len(depths))])
print(triplets)

triplet_sums = pd.Series([triplets[i -2] + triplets[i - 1] + triplets[i] for i in range(2, len(triplets))])
# for triplet in triplets:
#     print(triplet)

# triple_sums = pd.DataFrame(depths['value'] for i in range(len(depths))], columns=['triple_sum'])

# print(triple_sums)

# for i in range(len(triple_sums)):
#     if i == 0:
#         pass
#     elif triple_sums.iloc[i, 0] > triple_sums.iloc[i-1, 0]:
#         triple_sums.iloc[i, 1] = 1
#     else:
#         triple_sums.iloc[i, 1] = 0