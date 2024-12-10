class MemoryCell:
    def __init__(self, id: int, value: str):
        self.id = id
        self.value = value
        
    def __repr__(self):
        return self.value
    
    def checksum(self):
        return self.id * self.value