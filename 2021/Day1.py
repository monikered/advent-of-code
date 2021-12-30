# # How many measurements are larger than the previous measurement?

from numpy.core.numeric import NaN
import pandas as pd
import numpy as np

with open('./2021/inputs/day1.txt', 'r') as f:
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
print('The answer to part one is '+ str(np.sum(depths['change'])))

# # PART TWO

# this is so messy but hey it works

triplets = pd.DataFrame([depths.iloc[int(i):int(i)+3, 0] for i in range(len(depths))])
triplet_sums = pd.Series([triplets[i -2] + triplets[i - 1] + triplets[i] for i in range(2, len(triplets))])
triplet_sums_as_df = pd.DataFrame([np.max(triplet_sums[i]) for i in range(len(triplet_sums))])
triplet_sums_as_df['change'] = np.NaN

print(triplet_sums_as_df)

for i in range(len(triplet_sums_as_df)):
    if i == 0:
        pass
    elif triplet_sums_as_df.iloc[i, 0] > triplet_sums_as_df.iloc[i-1, 0]:
        triplet_sums_as_df.iloc[i, 1] = 1
    else:
        triplet_sums_as_df.iloc[i, 1] = 0

# The answer is 1497
print('The answer to part two is '+ str(np.sum(triplet_sums_as_df['change'])))