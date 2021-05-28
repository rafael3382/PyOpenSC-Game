"""BlocksDataFile = open("appearance/Content/BlocksData.txt")
BlocksData = BlocksDataFile.read()
BlocksDataFile.close()


Lines = BlocksData.split("\n")
SplitTable = Lines[0].split(";")
tmpDataBlock = {}
FinalBlockData = {}


for Line in Lines[1:]:
    Values = Line.split(";")
    for Index in range(0, len(Values)):
        tmpDataBlock[SplitTable[Index]] = Values[Index]
    FinalDataBlock
print(str(FinalData).replace(",", ",\n"))
"""
Blocks = {}
def AddToBlocks(String):

    for kov in String.split(" "):
        print(kov)
        Key, Value = kov.split("=")
        Blocks[Key] = Value
        
tmp = ""
with open("appearance/Content/BlocksData.xml") as BlocksFile:
    previous_line = ""
    for line in BlocksFile.read().split("\n"):
        if line.startswith("BlockId") and previous_line:
            AddToBlocks(tmp)
            tmp = ""
        tmp += line
        previous_line = line
        
            
