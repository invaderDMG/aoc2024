# Day 05 - Second puzzle

import math
from shared.utils import read_input

def main():
    orderingRules = orderingRulesExtraction()
    input_updatePages = read_input("day05/updatePages.txt")
    middlePageSum = 0

    for row in range(len(input_updatePages)):
        pages = input_updatePages[row].split(",")
        wrongPage = processRow(pages, orderingRules)
        if(wrongPage):
            middleTerm = math.floor(len(pages)/2)
            middlePageSum+=int(pages[middleTerm])
    print(middlePageSum)

def processRow(pages, orderingRules):
    wrongPage = False
    for i in range(len(pages)-1):
        for j in range(i+1, len(pages)):
            if (checkPair(pages, i, j, orderingRules)):
                wrongPage = True
                print("encontrado error")
                fixPair(pages, i, j)
    
    return wrongPage

def fixPair(pages, i, j):
    aux = pages[i]
    pages[i] = pages[j]
    pages[j] = aux

def checkPair(pages, a, b, orderingRules):
    print(pages[a], ",", pages[b], "?")
    return pages[b] in orderingRules and pages[a] in orderingRules[pages[b]]

def orderingRulesExtraction():
    input_orderingRules = read_input("day05/orderingRules.txt")

    orderingRules = {}
    for i in range(len(input_orderingRules)):
        x, y = input_orderingRules[i].split("|")
        if x not in orderingRules:
            orderingRules[x] = []
        orderingRules[x].append(y)
    
    return orderingRules

main()