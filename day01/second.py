# Day 01
from shared.utils import read_input, transform_input

def main():
    input_data = read_input("day01/input.txt")

    first_list, second_list = transform_input(input_data)

    total_similarity = 0
    similarity_map = {}
    for a in first_list:
        similarity_map[a] = findSimilarity(a, second_list)
        total_similarity += a*similarity_map[a]

    print("Total similarity is ", total_similarity)


def findSimilarity(needle, haystack):
    similarity = 0
    for a in haystack:
         if a == needle:
             similarity += 1

    return similarity

main()