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

def test_validator():
    assert validator(test_input) == 2, 'Should be 2 valid passports'

if __name__ == '__main__':
    if run_test:
        with open('./inputs/day4_test.txt', 'r') as test_input:
            test_validator()
            print('Test passed')
    else:
        with open('./inputs/day4.txt', 'r') as f:
            my_password_list = f.read()
            print(validator(my_password_list))