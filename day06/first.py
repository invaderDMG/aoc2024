# Day 06 - First puzzle

from typing import Set
from day06.guard import Guard
from day06.map import Map
from day06.position import Position
from shared.utils import read_input


def main():
    input_data = read_input("day06/test_input.txt")
    height = len(input_data)
    width = len(input_data[0])
    obstacle: Set[Position] = set()
    
    for verticalIndex in range(len(input_data)):
        for horizontalIndex in range(len(input_data[verticalIndex])):
            match input_data[verticalIndex][horizontalIndex]:
                case '#':
                    obstacle.add(Position(horizontalIndex, verticalIndex))
                case '^'|'>'|'V'|'<':
                    guardPosition = Position(horizontalIndex, verticalIndex)
            
    map = Map(width, height, Guard(guardPosition, "^"), obstacle)
    while(not map.guardOut()):
        map.loop()

    print(map)
    print(len(map.path))
    
main()
