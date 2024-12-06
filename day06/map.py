from typing import Set
from day06.guard import Guard
from day06.position import Position


class Map:
    def __init__(self, width: int, height: int, guard: Guard, obstacle: Set[Position]):
        self.width = width
        self.height = height
        self.guard = guard
        self.obstacle = obstacle
        self.path: Set[Position] = set()
        self.updateRepresentation()
        

    def __repr__(self):
        map = ''
        
        for i in range(len(self.representation)):
            for j in range(len(self.representation[i])):
                map += self.representation[i][j]
            map = map + "\n"
            
        return map

    def updateRepresentation(self):
        self.representation = [["." for _ in range(self.width)] for _ in range(self.height)]
        for obstacle in self.obstacle:
            self.representation[obstacle.vertical][obstacle.horizontal] = '#'
        for walkedPath in self.path:
            self.representation[walkedPath.vertical][walkedPath.horizontal] = 'X'
        if (not self.guardOut()):
            self.representation[self.guard.vertical][self.guard.horizontal] = self.guard.direction
        
            
    def loop(self):
        nextStep = self.guard.nextStep()
        if nextStep in self.obstacle:
            self.guard.turn()
        else:
            self.path.add(Position(self.guard.horizontal, self.guard.vertical))
            self.guard.move()
        self.updateRepresentation()
        
    def guardOut(self):
        return self.guard.horizontal == self.width or self.guard.vertical == self.height or self.guard.horizontal < 0 or self.guard.vertical < 0