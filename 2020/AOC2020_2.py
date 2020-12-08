#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:17:07 2020

@author: monicaremmers
"""

import re
total_valid = 0 # resets for each run

def PasswordParser(line):
    global total_valid
    m = re.findall(r'\d+', line) # finds the numbers within the string
    letter = re.search(r'[a-z]', line).group(0)
    pw = re.search(r'[a-z]+$', line).group(0)
    if pw.count(letter) in range(int(m[0]),int(m[1])+1):
        total_valid += 1
    print(total_valid) 
        
print('Please enter list of passwords.')
passwords = [ x for x in input().split('\n')]

for line in passwords:
    PasswordParser(line)
    
#%%

## Part Two
import re
total_valid = 0 # resets for each run   

def NewPasswordParser(line):
    global total_valid
    m = re.findall(r'\d+', line)    
    letter = re.search(r'[a-z]', line).group(0)
    pw = re.search(r'[a-z]+$', line).group(0)
    if (pw[int(m[0])-1]==letter) != (pw[int(m[1])-1]==letter):
        total_valid += 1
    print(total_valid)
    
print('Please enter list of passwords.')
passwords = [ x for x in input().split('\n')]

for line in passwords:
    NewPasswordParser(line)
    