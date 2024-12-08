# Day 08 - Second puzzle

from typing import List, Set

from day06.position import Position
from day08.antenna import Antenna
from shared.utils import read_input


def main():
    input_data = read_input("day08/input.txt")
    antennas: List[Antenna] = []
    width = len(input_data)
    height = len(input_data[0])
    
    for row in range(len(input_data)):
        for column in range(len(input_data[row])):
            if input_data[row][column] != '.':
                antennas.append(Antenna(input_data[row][column], Position(column, row)))

    antinodes: Set[Position] = set()
    antennasPerFrequence: dict[str, list[Antenna]] = {}
    for antenna in antennas:
        if antenna.frequency not in antennasPerFrequence:
            antennasPerFrequence[antenna.frequency] = []
        antennasPerFrequence[antenna.frequency].append(antenna)
    for frequency, antennas in antennasPerFrequence.items():
        if (len(antennas) > 1):
            for i in range(len(antennas)):
                for j in range(i + 1, len(antennas)):
                    foundAntinodes = findAntinodes(antennas[i], antennas[j], width, height)
                    antinodes.update(foundAntinodes)

    print(len(antinodes))
    
def findAntinodes(a: Antenna, b: Antenna, width: int, height: int) -> List[Position]:
    horizontalDifference = b.position.horizontal - a.position.horizontal
    verticalDifference = b.position.vertical - a.position.vertical
    antinodes: Set[Position] = set()
    anchor = Position(b.position.horizontal, b.position.vertical)
    while anchor.horizontal >=0 and anchor.horizontal < width and anchor.vertical >=0 and anchor.vertical < height:
        antinodes.add(Position(anchor.horizontal, anchor.vertical))
        anchor.horizontal += horizontalDifference
        anchor.vertical += verticalDifference
    anchor = Position(a.position.horizontal, a.position.vertical)
    while anchor.horizontal >=0 and anchor.horizontal < width and anchor.vertical >=0 and anchor.vertical < height:
        antinodes.add(Position(anchor.horizontal, anchor.vertical))
        anchor.horizontal -= horizontalDifference
        anchor.vertical -= verticalDifference
        
    return antinodes
    
    
main()