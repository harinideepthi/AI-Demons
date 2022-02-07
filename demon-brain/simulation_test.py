#notneeded any more.... blender simulation stuff
import bpy
import sys
import time
import json
sys.path.append('C:\\Users\\akash\\PycharmProjects\\ai')

from simulation import *

dio = bpy.data.objects["dio"]
diablo.pos = Position(0,0,0)
dio.location[0] = diablo.pos.x
dio.location[1] = diablo.pos.y
dio.location[2] = diablo.pos.z
print(diablo.pos)

vision = diablo.vision()
def render():
    for i in range(len(vision)):
        temp_object = bpy.data.objects[str(vision[i].id)].copy()
        temp_object.data = bpy.data.objects[str(vision[i].id)].data.copy()
        temp_object.animation_data_clear()
        bpy.context.collection.objects.link(temp_object)
        temp_object.name = str(vision[i].pos[0])+'&'+str(vision[i].pos[1])+'&'+str(vision[i].pos[2])
        with open('C:\\Users\\akash\\PycharmProjects\\ai\\jsonFiles\\loadedObj.json') as f:
            data = json.load(f)
            data.append(temp_object.name)
            
        with open('C:\\Users\\akash\\PycharmProjects\\ai\\jsonFiles\\loadedObj.json','w') as f:    
            json.dump(data,f)        
        
        
        temp_object.location[0]=vision[i].pos[0]
        temp_object.location[1]=vision[i].pos[1]
        temp_object.location[2]=vision[i].pos[2]
        
    
def delete_sim_objects():    
    for i in range(len(memory_objects)):
        bpy.data.objects.remove(bpy.data.objects[str(memory_objects[i])], do_unlink=True)
        

render()