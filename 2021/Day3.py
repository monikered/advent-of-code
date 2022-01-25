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
        binary_rate = ''.join([str(int(g)) for g in gamma_list])
    if rate == 'epsilon':
        epsilon_list = np.bitwise_not(gamma_list)
        binary_rate = ''.join([str(int(e)) for e in epsilon_list])
    decimal_rate = int(binary_rate, 2)
    return decimal_rate

def oxygen_generator_rating():
    pass

def co2_scrubber_rating():
    pass

def part_one():
    modes = vertical_list_slicer()
    gamma = rate_toggle_decimal(mode_list=modes, rate='gamma')
    epsilon = rate_toggle_decimal(mode_list=modes, rate='epsilon')
    res = f'PART ONE: The gamma rate is {gamma} and the epsilon rate is {epsilon}.\n The power consumption--their product--is {gamma*epsilon}.'
    print(res)

def part_two():
    modes = vertical_list_slicer()
    pass

if __name__ == '__main__':
    part_one()
    part_two()