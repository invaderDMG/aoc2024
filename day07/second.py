# Day 07 - Second puzzle

from typing import List

from shared.utils import read_input


def main():
    sumResults = 0
    input_data = read_input("day07/input.txt")
    for line in input_data:
        foundSolution = False
        result_str, operands_str = line.split(": ")
        result = int(result_str)
        operands = list(map(int, operands_str.split()))
        
        expressions = generate_results(operands)
        for expr in expressions:
            if expr == result and not foundSolution:
                foundSolution = True
                sumResults+=result
                
                
    print(sumResults)
    
def generate_results(operands: List[int]) -> List[int]:
    def helper(index: int, current_value: int) -> List[int]:
        if index == len(operands):
            return [current_value]

        results = []
        next_operand = operands[index]

        results += helper(index + 1, current_value + next_operand)
        results += helper(index + 1, current_value * next_operand)
        results += helper(index + 1, int(str(current_value) + str(next_operand)))

        return results

    return helper(1, operands[0])

main()