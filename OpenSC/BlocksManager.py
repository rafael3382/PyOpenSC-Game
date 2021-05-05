BlocksDataFile = open("appearance/Content/BlocksData.txt")
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
