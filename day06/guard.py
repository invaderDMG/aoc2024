from day06.position import Position


class Guard:
    def __init__(self, position: Position, direction: str):
        self.horizontal = position.horizontal
        self.vertical = position.vertical
        self.direction = direction

    def __repr__(self):
        return f"Guard(horizontal={self.horizontal}, vertical={self.vertical}, direction='{self.direction}')"
    
    def nextStep(self):
        nextStep = Position(self.horizontal, self.vertical)
        match self.direction:
            case '^':
                nextStep.vertical-=1
            case '>':
                nextStep.horizontal+=1
            case 'V':
                nextStep.vertical+=1
            case '<':
                nextStep.horizontal-=1
        
        return nextStep
    
    def move(self):
        nextStep = self.nextStep()
        self.horizontal = nextStep.horizontal
        self.vertical = nextStep.vertical
    
    def turn(self):
        match self.direction:
            case '^':
                self.direction='>'
            case '>':
                self.direction='V'
            case 'V':
                self.direction='<'
            case '<':
                self.direction='^'