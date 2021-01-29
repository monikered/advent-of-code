#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:32:21 2020

@author: monicaremmers
"""
import re

run_test = False

def part_one_validator(passports):
    ValidPassports = 0
    field_list = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
    fields = re.compile('|'.join(field_list))
    for passport in passports:
        if len(fields.findall(passport)) == 7:
            ValidPassports += 1
        else:
            pass
    return ValidPassports

def part_two_validator(passports):
    ValidPassports = 0
    # define valid fields
    field_list = ['byr:(19[2-9]\d|200[0-2])', 'iyr:(201\d|2020)', 
                  'eyr:(202\d|2030)', 'hgt:1([5-8]\d|9[0-3])cm|hgt:(59|6\d|7[0-3])in',
                  'hcl:#[a-z0-9]{6,}', 'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
                  'pid:\d{9,}']
    fields = re.compile('|'.join(field_list))
    for passport in passports:
        if len(fields.findall(passport)) == 7:       
            ValidPassports += 1
        else:
            pass
    return ValidPassports

def test_validator(test_input):
    assert part_one_validator(test_input) == 2, 'Should be 2 valid passports'

if __name__ == '__main__':
    if run_test:
        with open('./inputs/day4_test.txt', 'r') as test_input:
            test_validator(test_input.read().split('\n\n'))
            print('Test passed')
    else:
        with open('./inputs/day4.txt', 'r') as f:
            passports = f.read().split('\n\n')
            print('The number of valid passports in part one is {}.'.format(part_one_validator(passports)))
            print('The number of valid passports in part two is {}.'.format(part_two_validator(passports)))