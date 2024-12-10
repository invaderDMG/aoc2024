# Day 09 - First puzzle
from day09.memory import Memory
from shared.utils import read_input

def main():
    row = read_input("day09/input.txt")[0]
    # row = "12345"
    memory = Memory()
    
    for i in range(len(row)):
        if i % 2 == 0:
            memory.addFile(int(row[i]))
        else:
            memory.addFreeSpace(int(row[i]))
    
    # print(memory)
    
    print("starts compacting")
    while str(memory)[-memory.totalFreeMemory:] != "." * memory.totalFreeMemory:
        memory.compact()
        # print("compactedcheck", str(memory)[-memory.totalFreeMemory:])
    
    print("finished compacting")
    # print(memory)
    print(memory.checksum())
    # print(memory.memoryMap)
        

main() 