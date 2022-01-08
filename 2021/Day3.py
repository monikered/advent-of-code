import numpy as np
from statistics import mode

with open('./2021/inputs/day3test.txt', 'r') as f:
    diagnostic = f.read().strip().split("\n")

# THIS DOESN'T WORK BECAUSE THE INPUT (UNLIKE THE TEST DATA
# -- I HAVE 5 HARDCODED. 

# TODO: MAKE VERTICAL_SLICE_LIST() WORK FOR ANY LENGTH
def vertical_slice_list(binary):
    bit1 = [int(str(n[0])) for n in binary] 
    bit2 = [int(str(n[1])) for n in binary]
    bit3 = [int(str(n[2])) for n in binary]
    bit4 = [int(str(n[3])) for n in binary]
    bit5 = [int(str(n[4])) for n in binary]
    return bit1,bit2,bit3,bit4,bit5
def vertical_slice_test(binary):
    for i, char in enumerate(binary[0]): # this is CORRECT for the outer part of the loop!!!
        print([int(str(n[i])) for n in binary[i]])

# TODO: TURN GAMMA_BINARY INTO A FUNC USING LIST COMPREHENSION
# TODO: MORE PRECISE FUNCTION NAME
# TODO: COLLAPSE VERTICAL_SLICE_LIST() AS A FUNC
def rate_toggle_decimal(rate, binary_source=diagnostic):
    bit1, bit2, bit3, bit4, bit5 = vertical_slice_list(binary_source)
    gamma_binary = str(mode(bit1)) + str(mode(bit2)) + str(mode(bit3)) + str(mode(bit4)) + str(mode(bit5))

    if rate == 'gamma':
        gamma_decimal = int(gamma_binary, 2)
        return gamma_decimal
    if rate == 'epsilon':
        gamma_list = np.array([int(g) for g in gamma_binary], dtype=bool)
        epsilon_list_bool = np.bitwise_not(gamma_list)
        epsilon_binary = ''.join([str(int(e)) for e in epsilon_list_bool])
        epsilon_decimal = int(epsilon_binary, 2)
        return epsilon_decimal
    else:
        print('Not a recognized rate')

def part_one():
    gamma = rate_toggle_decimal(rate='gamma')
    epsilon = rate_toggle_decimal(rate='epsilon')
    res = f'The gamma rate is {gamma} and the epsilon rate is {epsilon}. The power consumption--their product--is {gamma*epsilon}.'
    print(res)
# power_consumption = gamma_int * epsilon_int

if __name__ == '__main__':
    vertical_slice_test(diagnostic)