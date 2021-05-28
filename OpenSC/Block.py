# Import Area
import json


#-------------


class Block:
    def __init__(self, x, y, z, typ3, color=None, Data=None):
        self.x, self.y, self.z, self.typ3, self.color = x, y, z, int(typ3), color
        self.data = Data
        self.IsCompreesed = False
    def return_me(self):
        return self.x, self.y, self.z, self.typ3#, color, data
    def Compare(self, AnotherObj):
        return self.x == AnotherObj.x and self.y == AnotherObj.y and self.z == AnotherObj.z and self.typ3 == AnotherObj.typ3 and self.color == AnotherObj.color and self.data == AnotherObj.data
class CompreesedBlock():
    def __init__(self, xstart, ystart, zstart, xend, yend, zend, typ3):
        self.xstart, self.ystart, self.zstart = xstart, ystart, zstart
        self.xend, self.yend, self.zend = xend, yend, zend
        self.typ3 = typ3
        self.IsCompreesed = True
    def AddBlock(self, block):
        self.xend = block.x
        self.yend = block.y
        self.zend = block.z
    def RRange(self, Start, End):
        if Start == End:
            return [Start]
        else:
            return range(Start, End+1)
    def Generate(self):
        xstart, ystart, zstart, xend, yend, zend, typ3 = self.xstart, self.ystart, self.zstart, self.xend, self.yend, self.zend, self.typ3
        Blocks = []
        if zstart == zend:
            if ystart == yend:
                if xstart == xend:
                    raise Exception("Same Block, Unnecessary!")
        for x in self.RRange(xstart, xend):
            for y in self.RRange(ystart, yend):
                for z in self.RRange(zstart, zend):
                    Blocks.append(Block(x,y,z, typ3))
        return Blocks





def is_row(Block, Next):
    xdiff = Next.x - Block.x
    ydiff = Next.y - Block.y
    zdiff = Next.z - Block.z
    Result = False
    definitivefalse = False
    DiffArr = [xdiff, ydiff, zdiff]
    
    for Diff in DiffArr:
        if Diff == 1:
            Result = True
        elif (not Diff == 0):
            return False
    return Result

def CompressBlocks(Blocks):
    CompreesedBlocks = {}
    
    InCompreesedBlock = False
    OtherBlocks = {}
    ActualBlock = 0
    while ActualBlock <= len(Blocks)-2:
        Block = Blocks[ActualBlock]
        NextBlock = Blocks[ActualBlock+1]
        if Block.IsCompreesed or NextBlock.IsCompreesed:
            raise Exception("BlockDict without BlockCompression is required")
        x, y, z = Block.x, Block.y, Block.z
        nextx, nexty, nextz = NextBlock.x, NextBlock.y, NextBlock.z 
        if (is_row(Block, NextBlock)) and NextBlock.typ3 == Block.typ3:
            if InCompreesedBlock:
                
                CompreesedBlocks[CompreesedBlocks.keys[len(CompreesedBlocks.keys) - 1]].AddBlock(NextBlock)
            else:
                CompreesedBlocks.append(CompreesedBlock(x,y,z,nextx,nexty,nextz, Block.typ3))
            InCompreesedBlock = True
        else:
            CompreesedBlocks[(Block.x, Block.y, Block.z)] = Block # organization should never be lost in a world, so we put everything on the same list 
            InCompreesedBlock = False
        ActualBlock += 2
    return CompreesedBlocks
class AllBlocks():
    def __init__(self):
        self.Blocks = {}
    def Search(self, Name):
        for block in self.Blocks.values():
            if block["Name"] == Name:
                return block["BlockId"]
                
    def Parse(self):
        Raw = eval(open("appearance/Content/BlocksData.xml").read())
        
        for Block in Raw:
            self.Blocks[Block["BlockId"]] = Block
    def GetTexture(self, Id):
        if Id == None:
            Id = "1"
        Id = str(Id)
        Result = ["0, 0", "0, 0", "0, 0", "0, 0", "0, 0", "0, 0"]
        if "Textures" in self.Blocks[Id]:
            if "TopTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[0] = self.Blocks[Id]["Textures"]["TopTextureLocation"]
            if "DownTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[5] = self.Blocks[Id]["Textures"]["TopTextureLocation"]
            if "BackTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[1] = self.Blocks[Id]["Textures"]["TopTextureLocation"]
            if "RightTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[2] = self.Blocks[Id]["Textures"]["TopTextureLocation"]
            if "LeftTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[3] = self.Blocks[Id]["Textures"]["TopTextureLocation"]
            if "FrontTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[4] = self.Blocks[Id]["Textures"]["TopTextureLocation"]
            if "SidesTextureLocation" in self.Blocks[Id]["Textures"]:
                Result[1] = self.Blocks[Id]["Textures"]["SidesTextureLocation"]
                Result[2] = self.Blocks[Id]["Textures"]["SidesTextureLocation"]
                Result[3] = self.Blocks[Id]["Textures"]["SidesTextureLocation"]
                Result[4] = self.Blocks[Id]["Textures"]["SidesTextureLocation"]
        else:
            Pos = self.Blocks[Id]["TextureLocation"]
            Result[0] = Pos
            Result[1] = Pos
            Result[2] = Pos
            Result[3] = Pos
            Result[4] = Pos
            Result[5] = Pos
        IntResult = []
        for Face in Result:
            IntResult.append(eval(f"[{Face}]"))
        return IntResult
