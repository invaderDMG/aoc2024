class File:
    def __init__(self, id: int, size: int):
        self.id = id
        self.size = size
        
    def __repr__(self):
        return f"#File(id='{self.id},size={self.size}')"