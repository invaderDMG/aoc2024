# Day 03 - Second puzzle

from shared.utils import read_input


def main():
    input_data = read_input("day03/input.txt")
    foundOperations = []
    enablingOperations = True;
    for row in range(len(input_data)):
        corruptedMemory = input_data[row]
        cursor=0
        i = 0
        while i < len(corruptedMemory):
            do = findDo(i, i+4, corruptedMemory)
            if (do):
                enablingOperations = True;
            dont = findDont(i, i+7, corruptedMemory)
            if (dont):
                enablingOperations = False
            operation = findMul(i, i+4, corruptedMemory)
            if (operation != [] and enablingOperations):
                foundOperations.append(operation)
            i+=1
    
    total = 0
    for i in range(len(foundOperations)):
        total += int(foundOperations[i][1]) * int(foundOperations[i][2])

    print("total of found operations is", total)

def findDo(i, cursor, corruptedMemory):
    if (corruptedMemory[i:cursor] == "do()"):
        return True
    return False

def findDont(i, cursor, corruptedMemory):
    if (corruptedMemory[i:cursor] == "don't()"):
        return True
    return False

def findMul(i, cursor, corruptedMemory):
    if (corruptedMemory[i:cursor] == "mul("):
        number1 = findNumber(corruptedMemory, cursor)
        if (number1 == ''):
            i+=cursor
        else:
            cursor += len(number1)
            comma = findSymbol(corruptedMemory, cursor, ",")
            if (comma != ''):
                cursor += 1
                number2 = findNumber(corruptedMemory, cursor)
                if (number2 != ''):
                    cursor += len(number2)
                    closingParenthesis = findSymbol(corruptedMemory, cursor, ")")
                    if (closingParenthesis != ''):
                        cursor += 1
                        return [corruptedMemory[i:cursor], number1, number2]
    
    return []
            
def findNumber(corruptedMemory, index):
    number = ''
    if (not corruptedMemory[index].isdigit()):
        return number
    number += corruptedMemory[index]
    if (not corruptedMemory[index+1].isdigit()):
        return number
    number += corruptedMemory[index+1]
    if (not corruptedMemory[index+2].isdigit()):
        return number
    number += corruptedMemory[index+2]
    if (corruptedMemory[index+3].isdigit()):
        return ''

    return number

def findSymbol(corruptedMemory, index, symbol):
    if (corruptedMemory[index] == symbol):
        return symbol
    else:
        return ''
    
main()