#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:32:21 2020

@author: monicaremmers
"""
import re

run_test = False

def validator(passport_list):
    passports = passport_list.split('\n\n')
    counter = 0
    field_list = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
    fields = re.compile('|'.join(field_list))
    for passport in passports:
        if len(fields.findall(passport)) == 7:
                counter += 1
        else:
            pass
    return counter
    

test_input = '''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
''' 

def test_validator():
    assert validator(test_input) == 2, 'Should be 2 valid passports'

if __name__ == '__main__':
    if run_test:
        test_validator()
        print('Test passed')
    else:
        with open('./inputs/day4.txt', 'r') as f:
            my_password_list = f.read()
            print(validator(my_password_list))