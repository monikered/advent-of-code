import numpy as np
from statistics import mode, multimode

with open('./2021/inputs/day3test.txt', 'r') as f:
    diagnostic = [[int(n) for n in line.strip()] for line in f.readlines()]

def mode_of_vertical_slice(rounding, binary=diagnostic):
    # takes a list of lists as input and returns the modal value of each column
    # of the stacked lists (as a list)
    modes = []

    if rounding == 'off':
        for i in range(len(binary[0])):
            modes.append(mode([n[i] for n in binary]))

    if rounding == 'up':
        for i in range(len(binary[0])):
            modes.append(max(multimode([n[i] for n in binary])))

    if rounding == 'down':
        for i in range(len(binary[0])):
            modes.append(min(multimode([n[i] for n in binary])))
    print(modes, np.array([bit for bit in modes]))
    return modes

def rate_toggle_decimal(mode_list, rate):
    input_list = np.array([bit for bit in mode_list], dtype=bool)
    if rate == 'gamma':
        gamma_list = input_list
        binary_rate = ''.join([str(int(g)) for g in gamma_list])
    if rate == 'epsilon':
        # epsilon list is just an inversion of gamma list
        epsilon_list = np.bitwise_not(input_list)
        # this could be extracted from here and the above if block
        binary_rate = ''.join([str(int(e)) for e in epsilon_list])
    decimal_rate = int(binary_rate, 2)
    return decimal_rate

# TODO: troubleshoot this function
def oxygen_generator_rating():
    o2_modes = mode_of_vertical_slice(rounding='up') # the modes of the whole list
    numbers = diagnostic # the options to choose from
    while len(numbers) > 1:
        for i in range(len(numbers[0])):
            # only keep the numbers where o2_modes[i] == numbers[][i] #something like this???

    pass

def co2_scrubber_rating():
    pass

def part_one():
    modes = mode_of_vertical_slice(rounding='off')
    gamma = rate_toggle_decimal(mode_list=modes, rate='gamma')
    epsilon = rate_toggle_decimal(mode_list=modes, rate='epsilon')
    res = f'PART ONE: The gamma rate is {gamma} and the epsilon rate is {epsilon}.\n The power consumption--their product--is {gamma*epsilon}.'
    return print(res)

def part_two():
    o2 = 0
    co2 = 0
    res = f'PART TWO: The oxygen generator rating is {o2} and the CO2 scrubber rating is {co2}.\n The life support rating--their product--is {o2*co2}.'
    return print(res)    

if __name__ == '__main__':
    part_one()
    # part_two()
    oxygen_generator_rating()