class oscworld:
    def __init__(self):
        self.Header = 'OpenSC_WorldBlockList_Header;'
        self.BlockMemory = []
        
    def New(self, path):
        WorldFile = open(path, "w+")
        World = WorldFile.write(header)
        WorldFile.close()
    def NewBlock(Type,
        
