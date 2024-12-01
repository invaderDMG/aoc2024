# Day 01
from shared.utils import read_input, transform_input

input_data = read_input("day01/input.txt")

first_list, second_list = transform_input(input_data)

first_list.sort()
second_list.sort()

total_difference = 0
for a, b in zip(first_list, second_list):
    total_difference += abs(a - b)

print("The sum total of the absolute differences is:", total_difference)