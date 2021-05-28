from Block import Block, CompreesedBlock, CompressBlocks
import struct
""" OpenSC Format
- what is .oscb?
OSCB is an acronym for O.pen.S.C.B.locks,




"""


class Not_OSCB_Error(Exception): pass
class InvalidOSCB(Exception): pass


class oscworld:
    def __init__(self):
        self.Header = b'OpenSC_WorldBlockList_Header;\n'
        self.BlockMemory = {}
    def New(self, path):
        WorldFile = open(path, "w+")
        World = WorldFile.write("")
        WorldFile.close()
    def Write(self, WorldArray, Blocks_oscb="Blocks.oscb"):
        #WorldArray = CompressBlocks(WorldArray)
        with open("Blocks.oscb", "a+b") as blocks:
            #print(WorldArray)
            for Block in WorldArray.values():
                if Block.IsCompreesed:
                    blocks.write(bytearray(str(Block.zstart), "utf8") + b" ")
                    blocks.write(bytearray(str(Block.ystart), "utf8") + b" ")
                    blocks.write(bytearray(str(Block.xstart), "utf8") + b" ")
                    blocks.write(bytearray(str(Block.zend), "utf8") + b" ")
                    blocks.write(bytearray(str(Block.yend), "utf8") + b" ")
                    blocks.write(bytearray(str(Block.xend), "utf8") + b" ")
                    blocks.write(bytearray(str(Block.typ3), "utf8") + b" " + b"\xA8\n")
                    continue
                x, y, z, typ3 = Block.return_me()
                blocks.write(typ3.to_bytes(2, byteorder='big'))
                blocks.write(bytearray(str(z), "utf8") + b" ")
                blocks.write(bytearray(str(y), "utf8") + b" ")
                blocks.write(bytearray(str(x), "utf8") + b" ")
                blocks.write(b'\xC9')
                blocks.write(bytearray("57", "utf8"))
                blocks.write(b'\xC9')
                blocks.write(bytearray("57", "utf8"))
                blocks.write(b"\n")
        print("Saved")
    def Read(self, ModelObj, Blocks_oscb="Blocks.oscb"):
        BlocksMemory = {}
        Chunks32h = open("Chunks32h.dat", "r+b")
        def Get_Chunk_Index(index):
            ChunkSize = 263184
            DictionarySize = 65537 * 12 # Entries * 12 bytes
            ChunkHeaderSize = 0
            ChunkIndex = index # No Header or Dictionary yet
            ChunkIndex *= ChunkSize
            ChunkIndex += DictionarySize
            
            #ChunkIndex += ChunkHeaderSize
            #print(ChunkIndex)
            return ChunkIndex
        def ReadBlocks(Chunks, X, Z, index):
            Chunks.seek(index)
            if Chunks.read(4) == b"\xEF\xBE\xAD\xDE":
                Chunks.read(12)
                print("Its a Chunk")
            else:
                print("No No No")
                return
            for  x in range(0, 16):
                for z in range(0, 16):
                    for y in range(0, 256):
                        
                        BlockTypeOld = Chunks.read(1) 
                        BlockType = int.from_bytes(BlockTypeOld, "little", signed=False)#struct.unpack("<I", BlockTypeOld)[0]
                        #print(BlockType)
                        if BlockType == 0:
                            continue
                        if BlockType < 0:
                            print(BlockType)
                            exit()
                        ModelObj.add_block((X+x, y, Z+z), BlockType, False)
                        Chunks.read(3) # Skip other data
        def ReadDictionaryAndExtractBlocks():
            bytes_readed = 0
            while bytes_readed < 65536 * 12:
                Chunks32h.seek(bytes_readed) # Go to Dictionary
                Entry = Chunks32h.read(12)
                x, z, index = struct.unpack("<iii", Entry)
                # Normalize
                x, z = x * 16, z * 16
                
                if not index == -1:
                    print("Hex:")
                    print(Entry.hex().upper())
                    print(f"X: {x} Z: {z} Index: {index}")
                    FileIndex = Get_Chunk_Index(index)
                    ReadBlocks(Chunks32h, x, z, FileIndex)
                    break
                bytes_readed += (4*3)
                
        ReadDictionaryAndExtractBlocks()
        Chunks32h.close()
        return
        PlayerPos = None
        with open(Blocks_oscb, "r+b") as OSCB:
            for Line in OSCB:
                if Line[:-1].endswith(b"\xa8"):
                    zstart, ystart, xstart, zend, yend, xend, typ3 = Line.split(b" ")[0:7]
                    xstart, ystart, zstart = int(xstart), int(ystart), int(zstart)
                    xend, yend, zend = int(xend), int(yend), int(zend)
                    typ3 = int(typ3)
                    BlocksCompreesed = CompreesedBlock(xstart, ystart, zstart, xend, yend, zend, typ3).Generate()
                    for BlockToAdd in BlocksCompreesed:
                        ModelObj.add_block((BlockToAdd.x,BlockToAdd.y,BlockToAdd.z), BlockToAdd.typ3, immediate=False)
                    continue
                Typ3 = int.from_bytes(Line[0:2], byteorder = "big")
                z, y, x = Line[2:].split(b" ")[:3]
                x, y, z = int(x), int(y), int(z)
                #print(x,y,z)
                ModelObj.add_block((x,y,z), Typ3, immediate=False)
        return BlocksMemory
    #def NewBlock(Type, X, Y, Z, Rotation=None):
        
