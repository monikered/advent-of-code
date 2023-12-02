import pytest
import re

def calibrate_part_one(line):
	for i, char in enumerate(line):
		if char.isdigit():
			first_digit = char
			break
	for i, char in enumerate(reversed(line)):
		if char.isdigit():
			last_digit = char
			break
	calibration_value = first_digit+last_digit
	return int(calibration_value)

def test_calibration_one():
	assert calibrate_part_one('1abc2') == 12

def test_calibration_two():
	assert calibrate_part_one('pqr3stu8vwx') == 38

def test_calibration_three():
	assert calibrate_part_one('a1b2c3d4e5f') == 15

def test_calibration_four():
	assert calibrate_part_one('treb7uchet') == 77

def calibrate_part_two(line):
	# will likely need to use re.search instead of isdigit()
	# UNLESS I use re.sub first to turn words into numbers
	# could use re.split to make a list...
	# using reversed() will not work unless I have a second list of numbers spelled backwards
	match = re.search('', line)

if __name__ == '__main__':
	with open('./inputs/day1.txt', 'r') as f:
		calibration_document = f.read().strip().split("\n")	
		print(f'The answer to part one is {sum([calibrate_part_one(l) for l in calibration_document])}')
		# tests for part two
		calibrate_part_two('two1nine')
		calibrate_part_two('eightwothree')
		calibrate_part_two('abcone2threexyz')
		calibrate_part_two('4nineeightseven2')
		calibrate_part_two('zoneight234')
		calibrate_part_two('7pqrstsixteen')

