from typing import List

from day09.file import File
from day09.memoryCell import MemoryCell

class Memory:
    def __init__(self):
        self.files: List[File] = []
        self.free: List[File] = []
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
        file = File(-1, size)
        self.free.append(file)
        for i in range(size):
            self.memoryMap.append(MemoryCell(len(self.memoryMap), '.'))
        self.totalFreeMemory += size
        
    def compact(self):
        lastFileCursor = self.getLastFileCursor()
        lastFile = self.files[int(self.memoryMap[lastFileCursor].value)]
        self.clear(lastFileCursor - lastFile.size +1, lastFileCursor)
        
        cursor = 0
        remainingFile = str(lastFile.id)*lastFile.size
        while cursor < len(self.memoryMap) and remainingFile != '':
            if (self.memoryMap[cursor].value == '.'):
                self.memoryMap = self.memoryMap[:cursor] + [MemoryCell(cursor, str(lastFile.id))] + self.memoryMap[cursor+1:]
                remainingFile = remainingFile[:-1*len(str(lastFile.id))]
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
    
class MemoryBlocks:
    def __init__(self):
        self.blocks: List[File] = []
        self.lastInsertedId = -1
        
    def __repr__(self):
        representation = ''
        for block in self.blocks:
            representation += '['+str(block.id)+']'
        return representation
    
    def memoryMap(self):
        representation = ''
        for block in self.blocks:
            if(block.id > -1):
                representation += str(block.id)*block.size
            else:
                representation += '.'*block.size
        return representation
    
    def addFile(self, size: int):
        self.lastInsertedId+=1
        file = File(self.lastInsertedId, size)
        self.addBlock(file)
        
        
    def addFreeSpace(self, size: int):
        freeSpace = File(-1, size)
        self.addBlock(freeSpace)
    
    def addBlock(self, file: File):
        self.blocks.append(file)
        
    def blockCompact(self):
        lastElementId = self.lastInsertedId
        while (lastElementId > 0):
            print(self)
            print("compacting",lastElementId)
            lastFileIndex = self.findFileIndexFromLastOne(lastElementId)
            if (lastFileIndex != -1):
                fittingCursor = self.findFittingSpace(lastFileIndex)
                if (fittingCursor != -1 and fittingCursor < lastFileIndex):
                    self.fitInEmptySpace(fittingCursor, lastFileIndex)
            lastElementId -= 1
            
    def findFileIndexFromLastOne(self, elementId):
        for index, element in reversed(list(enumerate(self.blocks))):
            if (element.id == elementId):
                return index
        return -1
            
    def fitInEmptySpace(self, fittingCursor, lastFileIndex):
        
        file = File(self.blocks[lastFileIndex].id, self.blocks[lastFileIndex].size)
        self.blocks[lastFileIndex].id = -1
        if (self.blocks[fittingCursor].size == file.size):
            self.blocks[fittingCursor].id = file.id
        else:
            self.blocks[fittingCursor].size -= file.size
            self.blocks.insert(fittingCursor, file)
             
    def findFittingSpace(self, id: int):
        cursor = 0
        while (cursor < len(self.blocks)):
            if (self.blocks[cursor].id == -1 and self.blocks[cursor].size >= self.blocks[id].size):
                return cursor
            cursor+=1
            
        return -1
    
    def checksum(self):
        checksum = 0
        indexCounter = 0
        while (len(self.blocks) > 0):
            if(self.blocks[0].id >= 0):
                checksum += indexCounter * self.blocks[0].id
                print(indexCounter,"*",self.blocks[0].id)
            self.blocks[0].size-=1
            if (self.blocks[0].size <= 0):
                del(self.blocks[0])
            indexCounter+=1
            
        return checksum