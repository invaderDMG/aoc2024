from typing import List

from day09.file import File
from day09.memoryCell import MemoryCell

class Memory:
    def __init__(self):
        self.cell = []
        self.files: List[File] = []
        self.free = []
        self.memoryMap: List[MemoryCell] = []
        self.totalFreeMemory = 0
        
    def __repr__(self):
        memoryMap = ''
        for memoryCell in self.memoryMap:
            memoryMap += memoryCell.value
            
        return memoryMap
    
    def addFile(self, size: int):
        file = File(len(self.files), size)
        self.files.append(file)
        for i in range(file.size):
            self.memoryMap.append(MemoryCell(len(self.memoryMap), str(file.id)))
        
        
    def addFreeSpace(self, size: int):
        self.free.append(size)
        for i in range(size):
            self.memoryMap.append(MemoryCell(len(self.memoryMap), '.'))
        self.totalFreeMemory += size
        
    def compact(self):
        
        lastFileCursor = self.getLastFileCursor()
        lastFile = self.files[int(self.memoryMap[lastFileCursor].value)]
        self.clear(lastFileCursor - lastFile.size +1, lastFileCursor)
        print("compacting file on [",lastFileCursor - lastFile.size +1, ",", lastFileCursor,"]", self.memoryMap[lastFileCursor].value)
        
        cursor = 0
        remainingFile = str(lastFile.id)*lastFile.size
        while cursor < len(self.memoryMap) and remainingFile != '':
            if (self.memoryMap[cursor].value == '.'):
                self.memoryMap = self.memoryMap[:cursor] + [MemoryCell(cursor, str(lastFile.id))] + self.memoryMap[cursor+1:]
                remainingFile = remainingFile[:-1]
            cursor+=1 

    def getLastFileCursor(self):
        lastFileCursor = len(self.memoryMap)
        
        fileFound = False
        while lastFileCursor >=0 and not fileFound:
            lastFileCursor-=1
            if (self.memoryMap[lastFileCursor].value != '.'):
                fileFound = True
        
        return lastFileCursor
    
    def clear(self, a: int, b: int):
        emptyMemoryCells = []
        for i in range(a, b+1):
            emptyMemoryCells.append(MemoryCell(i, '.'))
        self.memoryMap = self.memoryMap[:a] + emptyMemoryCells + self.memoryMap[b+1:]

    def checksum(self):
        checksum = 0
        for index, memoryCell in enumerate(self.memoryMap):
            if memoryCell.value != '.':
                checksum += index * int(memoryCell.value)
                # print(index, "*", int(memoryCell.value))
                
        return checksum