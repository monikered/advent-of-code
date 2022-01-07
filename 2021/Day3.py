from statistics import mode

with open('./2021/inputs/day3test.txt', 'r') as f:
    diagnostic = f.read().strip().split("\n")

def boolean_

def gamma(binary=diagnostic):
    bit1 = [int(str(n[0])) for n in binary] # you could turn this into a function
    bit2 = [int(str(n[1])) for n in binary]
    bit3 = [int(str(n[2])) for n in binary]
    bit4 = [int(str(n[3])) for n in binary]
    bit5 = [int(str(n[4])) for n in binary]
    gamma_bin = str(mode(bit1)) + str(mode(bit2)) + str(mode(bit3)) + str(mode(bit4)) + str(mode(bit5))
    return gamma_bin

def epsilon(gamma):
    # mask gamma to get epsilon?

power_consumption = gamma_int * epsilon_int