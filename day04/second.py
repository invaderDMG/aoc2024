# Day 04 - Second puzzle

from shared.utils import read_input

def main():
    input_data = read_input("day04/input.txt")
    countmas = 0

    for rowIndex in range(len(input_data)):
        for columnIndex in range(len(input_data[rowIndex])):
            countmas += read3x3matrix(input_data, rowIndex, columnIndex)

    print(countmas)

def read3x3matrix(input_data, i,j):
    rows = len(input_data)
    cols = len(input_data[0])

    if (i <= rows-3 and j <= cols -3):
        print(j)
        firstBranch = input_data[i][j] + input_data[i+1][j+1] + input_data[i+2][j+2]
        secondBranch = input_data[i+2][j] + input_data[i+1][j+1] + input_data[i][j+2] 
        if (firstBranch == "MAS" and secondBranch == "MAS") or (firstBranch == "SAM" and secondBranch == "SAM") or (firstBranch == "MAS" and secondBranch == "SAM") or (firstBranch == "SAM" and secondBranch == "MAS"):
            return 1
        
    return 0

def print3x3matrix(input_data, i,j):
    print(input_data[i][j], input_data[i][j+1], input_data[i][j+2])
    print(input_data[i+1][j], input_data[i+1][j+1], input_data[i+1][j+2])
    print(input_data[i+2][j], input_data[i+2][j+1], input_data[i+2][j+2])

main()