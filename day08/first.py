# Day 08 - First puzzle

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
                    foundAntinodes = findAntinodes(antennas[i], antennas[j])
                    if foundAntinodes[0].horizontal >= 0 and foundAntinodes[0].horizontal < width and foundAntinodes[0].vertical >= 0 and foundAntinodes[0].vertical < height:
                        antinodes.add(foundAntinodes[0])
                    if foundAntinodes[1].horizontal >= 0 and foundAntinodes[1].horizontal < width and foundAntinodes[1].vertical >= 0 and foundAntinodes[1].vertical < height:
                        antinodes.add(foundAntinodes[1])

    print(len(antinodes))
    
def findAntinodes(a: Antenna, b: Antenna) -> List[Position]:
    firstAntinode = Position(2*a.position.horizontal - b.position.horizontal, 2*a.position.vertical - b.position.vertical)
    secondAntinode = Position(2*b.position.horizontal - a.position.horizontal, 2*b.position.vertical - a.position.vertical)
    
    return [firstAntinode, secondAntinode]
    
    
main()