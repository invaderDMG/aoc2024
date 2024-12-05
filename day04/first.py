# Day 04 - First puzzle


from shared.utils import read_input

def main():
    input_data = read_input("day04/input.txt")
    xmasFound = 0
    horizontal = 0
    vertical = 0
    diagonal = 0
    for rowIndex in range(len(input_data)):
        for columnIndex in range(len(input_data[rowIndex])):
            horizontal+=findHorizontal(input_data[rowIndex][0:len(input_data[rowIndex])], columnIndex)
        vertical+=processVertical(input_data, rowIndex)
    diagonal+=findRegularDiagonal(input_data)
    diagonal+=findReverseDiagonal(input_data)
    print("How many times does XMAS appear?:")
    print("Horizontal: ", horizontal)
    print("Vertical: ", vertical)
    print("Diagonal: ", diagonal)
    print("total: ", diagonal+horizontal+vertical)

def findHorizontal(currentString, y):
    if (len(currentString) - y >= 4):
        possibleString = currentString[y:y+4]
        if (possibleString == "XMAS"):
            return 1
        if (possibleString == "SAMX"):
            return 1
    
    return 0

def processVertical(input_data, index):
    xmasFound = 0
    
    currentColumn=""
    for rowIndex in range(len(input_data)):
        currentColumn+=input_data[rowIndex][index]
    for columnIndex in range(len(currentColumn)):
        xmasFound+=findHorizontal(currentColumn, columnIndex)

    return xmasFound

def findRegularDiagonal(input_data):
    print("diagonales regulares")
    xmasFound = 0
    
    rows = len(input_data)
    cols = len(input_data[0])

    for col_start in range(cols):
        i, j = 0, col_start
        diagonal = []
        while i < rows and j >= 0:
            diagonal.append(input_data[i][j])
            i += 1
            j -= 1
        
        currentWord = "".join(diagonal)
        for columnIndex in range(len(currentWord)):
            xmasFound+=findHorizontal(currentWord, columnIndex)
        

    for row_start in range(1, rows):
        i, j = row_start, cols - 1
        diagonal = []
        while i < rows and j >= 0:
            diagonal.append(input_data[i][j])
            i += 1
            j -= 1

        currentWord = "".join(diagonal)
        for columnIndex in range(len(currentWord)):
            xmasFound+=findHorizontal(currentWord, columnIndex)

    return xmasFound

def findReverseDiagonal(input_data):
    print("diagonales inversas")
    xmasFound = 0

    rows = len(input_data)
    cols = len(input_data[0])

    for col_start in range(cols - 1, -1, -1):
        i, j = 0, col_start
        diagonal = []
        while i < rows and j < cols:
            diagonal.append(input_data[i][j])
            i += 1
            j += 1
        currentWord = "".join(diagonal)
        for columnIndex in range(len(currentWord)):
            xmasFound+=findHorizontal(currentWord, columnIndex)

    for row_start in range(1, rows):
        i, j = row_start, 0
        diagonal = []
        while i < rows and j < cols:
            diagonal.append(input_data[i][j])
            i += 1
            j += 1
        currentWord = "".join(diagonal)
        for columnIndex in range(len(currentWord)):
            xmasFound+=findHorizontal(currentWord, columnIndex)

    return xmasFound

main()