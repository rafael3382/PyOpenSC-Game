import numpy
class 3DArray:
    def __init__(self, XSize, YSize, ZSize):
        self.3DArray = {}

                  
    def __iter__(self):
        return self
    def add(X,Y,Z, Obj):
        
        
        self.3DArray[X][Y][Z] = 
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
