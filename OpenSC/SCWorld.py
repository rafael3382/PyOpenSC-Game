import sys, os
import zipfile
class Block():
    def  __init__(self, Type, Color=None, Data=None, Rotate=0, WireCubeFace=None): 
        self.Type, self.Color, self.Data, self.Rotate, self.WireCubeFace = Type, Color, Data, Rotate, WireCubeFace Color
    def Number0Format(self, Number, zeros=3):
        strint = str(Number)
        if len(strint) == 1:
    def ToOpenBlock(self):
        Result = f"{Type}"
        
class scworld2oscworld:
    def __init__(self):
        Info = {}
        BlocksExtracted = []
    
    def convert(self, Inp, Out):
        with ZipFile(Inp) as myzip:
            with myzip.open("Chunks32h.dat") as Dat:
        print(myfile.read())
if __name__ == "__main__":
    print("scworld2oscworld Converter Version 1.0")
    print("OpenSC Project")
    if len(sys.argv) <= 1:
        print(f"python {os.path.basename(__file__)} InputFile.scworld OutputFile.oscworld\nOr python {os.path.basename(__file__)} InputFileName.scworld\nOr python {os.path.basename(__file__)} InputFileName.scworld -o OutputFileName.scworld")
        exit()
    InputFile = ""
    OutputFile = ""
    Next_o = False
    for Number, Arg in enumerate(sys.argv[1:]):
        if Next_o:
            OutputFile = Arg
            Next_o = False
        if Arg == "-o":
            Next_o = True
            continue
        if  Number == 1 and os.path.exists(Arg):
            OutputFile = Arg
        if Number == 0 and os.path.exists(Arg):
            InputFile = Arg
    
            
