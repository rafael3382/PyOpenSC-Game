from PIL import Image

import json

class InvalidTexture(Exception):
    None

Cubes = {}
CubeSize = 32

im = Image.open('blocks.png')
width, height = im.size
if width % CubeSize or height % CubeSize:
    raise InvalidTexture("Invalid Resolution")

BlocksX = width // CubeSize
BlocksY = width // CubeSize
for BlockX in range(0, BlocksX):
    for BlockY in range(0, BlocksY):
        Cubes[f"ToBeNamed{BlockX}{BlockY}"] = ((BlockX*CubeSize, BlockY*CubeSize), ((BlockX*CubeSize+CubeSize, BlockY*CubeSize+CubeSize)))
with open("TextureMap.json", "w") as TexMap:
    TexMap.write(str(json.dumps(Cubes)).replace(",", ",\n"))



