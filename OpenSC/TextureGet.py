BlocksData = open("appearance/Content/BlocksData.txt")

Decoded = {}

Keys = BlocksData.readline().split(";")
BlocksData.readline()
BlocksData.readline()

ActualBlock = "NonBlock"




for Line in BlocksData.read().split("\n"):
    if Line.count(";") != len(Keys)-1: continue
    Values = Line.split(";")

    for KeyAdr, Value in enumerate(Values):
        Key = Keys[KeyAdr]
        if Key == "Class Name":
            ActualBlock = Value
            Decoded[ActualBlock] = {}
        else:
            Decoded[ActualBlock][Key] = Value



def DecodeTexture(name):
    try:
        Block = Decoded[name+"Block"]
        xy = int(Block["DefaultTextureSlot"])
    except:
        return 16,16
    
    y = xy // 16
    x = xy-y*16
    print(x,y)
    return x,y
DecodeTexture("Grass")









BlocksData.close()
