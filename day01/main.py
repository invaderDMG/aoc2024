# Day 01
from shared.utils import read_input, transform_input

# Leer la entrada del archivo
input_data = read_input("day01/input.txt")

# Transformar la salida de parse_input
first_list, second_list = transform_input(input_data)

first_list.sort()
second_list.sort()

# Calcular la suma de las diferencias absolutas
total_difference = 0
for a, b in zip(first_list, second_list):
    total_difference += abs(a - b)

print("La suma total de las diferencias absolutas es:", total_difference)