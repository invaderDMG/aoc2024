# Day 2 - First puzzle

from shared.utils import read_input


def main():
    input_data = read_input("day02/input.txt")
    safeReports = 0
    for a in input_data:
        if (checkSafeReport(list(map(int, a.split())))):
            safeReports+=1
    print("Safe reports: ",safeReports)

def checkSafeReport(report):
    direction = (report[0] - report[1] < 0)
    for i in range(1, len(report)):
        difference = report[i-1] - report[i]
        if ((difference < 0) != direction):
            return False
        if (abs(difference) <= 0 or abs(difference) > 3):
            return False
    
    return True
        

main()