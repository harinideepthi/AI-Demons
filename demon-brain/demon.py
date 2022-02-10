from functions import *
from classes  import *
import json
from math import dist


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
#method that loads chunk... it finds what are the object the posistion loads
    def chunk_loader(self, vr):
        loaded_chunks = []
        a = Position(self.x + vr, self.y, self.z + vr)
        b = Position(self.x + vr, self.y, self.z - vr)
        c = Position(self.x - vr, self.y, self.z + vr)
        d = Position(self.x - vr, self.y, self.z - vr)
        final = [a, b, c, d]
        loaded_objects=[]
        for i in final:
            loaded_chunks.append(chunkClassifier(i))
        with open('C:\\Users\\akash\\PycharmProjects\\ai\\jsonFiles\\worldData.json') as f:
            data = json.load(f)
            for i in loaded_chunks:
                i = str(int(i))
                try:

                    for j in range(len(data[i])):
                        temp_obj =objectCombine(data[i][j][0])
                        temp_obj.name=data[i][j][0]
                        temp_obj = SimObject(temp_obj,data[i][j][1],data[i][j][2],i,j)
                        loaded_objects.append(temp_obj)
                    print(f'succesfull loaded chunkno: {i}')
                except:
                    print(f'error loaded chunkno: {i}')
        return(loaded_objects)

#defining the class demon... demon is the creature that holds all the information ... it's the being we're creating
class Demon:
    def __init__(self, pos, char,visionRange):
        self.pos = Position(pos[0],pos[1],pos[2])
        self.char = char
        self.visionRange = visionRange

    def translate(self, pos):
        self.pos = pos
    def vision(self):
        vision =[]
        loaded_objects = self.pos.chunk_loader(self.visionRange)
        for i in loaded_objects:
            if dist(i.pos,[self.pos.x,self.pos.y,self.pos.z])<=self.visionRange:
                vision.append(i)

        return vision

