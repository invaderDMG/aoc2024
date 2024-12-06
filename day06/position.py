class Position:
    def __init__(self, horizontal: int, vertical: int):
        self.horizontal = horizontal
        self.vertical = vertical
        
    def __repr__(self):
        return f"({self.horizontal}, {self.vertical})"
    
    def __eq__(self, other: object):
        if not isinstance(other, Position):
            return NotImplemented
        return self.horizontal == other.horizontal and self.vertical == other.vertical
    
    def __hash__(self):
        return hash((self.horizontal, self.vertical))
