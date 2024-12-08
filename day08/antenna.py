from day06.position import Position


class Antenna:
    def __init__(self, frequency: str, position: Position):
        self.frequency = frequency
        self.position = position
        
    def __repr__(self):
        return f"Antenna(frequency='{self.frequency}: horizontal={self.position.horizontal}, vertical={self.position.vertical}')"