import numpy
class 3DArray:
    def __init__(self, XSize, YSize, ZSize):
        self.3DArray = []
        for x in range(0, ZSize+1):
            for y in range(0, YSize+1):
                for z in range(0, XSize+1):
                  
    def __iter__(self):
        return self
    def add(X,Y,Z, Obj):
        try:
            self.3DArray[X].append
        [].
        self.3DArray[X] = []
        self.3DArray[X][Y]
    def __getitem__(self, item):
        if item >= :
            raise IndexError("CustomRange index out of range")
        return 
    def __len__(self):
        return self.high - self.low
class RealGen:
    def __init__(self):
        self.Terrain = []
    def GenerateTree(self, Pos, Biome):
        Nonr
    def Generate(self, Seed, UserWorld, BiomeSize, PlayerPos, TerrainVisibility = 214):
        
        StartX = PlayerPos[0] - TerrainVisibility
        StartY = 0
        StartZ = PlayerPos[2] - TerrainVisibility
        StopX = PlayerPos[0] + TerrainVisibility
        StopY = 256
        StopZ = PlayerPos[2] + TerrainVisibility

        for x in range(StartX, StopX+1):
            for z in range(StartZ, StopZ+1):
                if and UserWorld[x][1][z] == "Air":
                    self.Terrain.append(["Bedrock", x,0,z])
        
        
Gen = RealGen()
print("Start")
for i in range(0, 50):
    Gen.Generate("test", [], 1, [0,0,0])
print("Done")
