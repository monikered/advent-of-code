import numpy as np
from statistics import mode

with open('./2021/inputs/day3.txt', 'r') as f:
    diagnostic = [[int(n) for n in line.strip()] for line in f.readlines()]

def vertical_list_slicer(binary=diagnostic):
    modes = []
    for i in range(len(binary[0])):
        modes.append(mode([n[i] for n in binary]))
    return modes

def rate_toggle_decimal(mode_list, rate):
    gamma_list = np.array([bit for bit in mode_list], dtype=bool)
    if rate == 'gamma':
        gamma_binary = ''.join([str(int(g)) for g in gamma_list])
        gamma_decimal = int(gamma_binary, 2)
        return gamma_decimal
    if rate == 'epsilon':
        epsilon_list = np.bitwise_not(gamma_list)
        epsilon_binary = ''.join([str(int(e)) for e in epsilon_list])
        epsilon_decimal = int(epsilon_binary, 2)
        return epsilon_decimal
    else:
        print('Not a recognized rate')

def part_one():
    modes = vertical_list_slicer()
    gamma = rate_toggle_decimal(mode_list=modes, rate='gamma')
    epsilon = rate_toggle_decimal(mode_list=modes, rate='epsilon')
    res = f'PART ONE: The gamma rate is {gamma} and the epsilon rate is {epsilon}.\n The power consumption--their product--is {gamma*epsilon}.'
    print(res)
# power_consumption = gamma_int * epsilon_int

if __name__ == '__main__':
    part_one()