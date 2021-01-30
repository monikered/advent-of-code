#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:02:51 2021

@author: monicaremmers
"""

# 128 rows on plane
# range(0, 127)
# first 7 characters are F (front) or B (back)
# div by 2 (midpoint), keep upper (B) or lower (F) half 
# repeat until one row remains
# 8 columns on plane
# range(0, 7)
# last 3 characters are L (lower) or R (upper)
# L = F and R = B
# [0-127] -> [0-63] -> [32-63] -> [32-47] etc
# seat ID = 8r + c
# goal = highest seat ID