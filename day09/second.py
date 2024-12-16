# Day 09 - Second puzzle
from day09.memory import MemoryBlocks
from shared.utils import read_input

def main():
    row = read_input("day09/test_input.txt")[0]
    memory = MemoryBlocks()
    
    for i in range(len(row)):
        if i % 2 == 0:
            memory.addFile(int(row[i]))
        else:
            memory.addFreeSpace(int(row[i]))
            
    # print(memory)
    # print(memory.memoryMap())
    
    print("starts compacting")
    memory.blockCompact()    
    print("finished compacting")
    
    print(memory.checksum())
        

main() 