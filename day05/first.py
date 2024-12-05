# Day 05 - First puzzle

import math
from shared.utils import read_input

def main():
    orderingRules = orderingRulesExtraction()
    input_updatePages = read_input("day05/updatePages.txt")
    middlePageSum = 0
    for i in range(len(input_updatePages)):
        pages = input_updatePages[i].split(",")
        pageIndex = 0
        ordered = True
        while (pageIndex < len(pages)-1) and ordered: 
            if (not checkOrderingRules(orderingRules, pages, pageIndex)):
                ordered = False
            pageIndex+=1
        
        if ordered:
            middleTerm = math.floor(len(pages)/2)
            middlePageSum+=int(pages[middleTerm])
    print(middlePageSum)
        

def checkOrderingRules(orderingRules, pages, previousPageIndex):
    pageIndex=previousPageIndex+1;
    ordered = True;
    while pageIndex < len(pages) and ordered:
        currentPage = pages[pageIndex]
        
        if (int(currentPage) in orderingRules and int(pages[previousPageIndex]) in orderingRules[int(currentPage)]):
            print(pages[previousPageIndex], "está en la lista de", currentPage, orderingRules[int(currentPage)])
            return False
        pageIndex+=1
    
    return True
        

def orderingRulesExtraction():
    input_orderingRules = read_input("day05/orderingRules.txt")

    orderingRules = {}
    for i in range(len(input_orderingRules)):
        x_str, y_str = input_orderingRules[i].split("|")
        x = int(x_str)
        y = int(y_str)
        if x not in orderingRules:
            orderingRules[x] = []
        orderingRules[x].append(y)
    
    return orderingRules

main()