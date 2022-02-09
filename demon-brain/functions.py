#importing shit

import json
from classes import *
from character import *
import time
import random

#derites function driver is a variable defined is character py.... don't forget imp things dumbass

def derites(driver,value):

  """

    description: converts driver values into derites using their corresponding pdex values
    parameter: driver(class: drive), value(int)
    returns: pdex*value
    driver: choose which driver the value belongs to
    value: given a value to convert into derites

  """

  if value<=driver.le:
    pdex=driver.pi1
  if value>driver.le and value<driver.ue :
    pdex=driver.pi2
  if value>=driver.ue:
    pdex=driver.pi3
  return pdex*value

#action extractor function returns action class from the name of the action
def action_extractor(aan):
    """

    description: converts a string into its corresponding action class.
    parameter: aan (string)
    returns: action object

    """


    with open('C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\action_dict.json') as f:
        data = json.load(f)
        act = action(data[aan]["tag_matrix"],matrix_to_ds(data[aan]["driver_state"]),matrix_to_ds(data[aan]["obs_pm"]),aan,data[aan]["mi_list"])

    return act

#obj extractor function return object class from the name fo the object
def object_extractor(word):
    """

     description: converts a string into its corresponding object class.
     parameter: word (string)
     returns: object object

     """
    with open("C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\object_dict.json") as f:
        data = json.load(f)
        property_driver=[]
        value_driver = driver_state(data[word]["driver"][0], data[word]["driver"][1], data[word]["driver"][2],
                                    data[word]["driver"][3], data[word]["driver"][4], data[word]["driver"][5], data[word]["driver"][6])
        for i in range(len(data[word]["properties"])):
            property_driver.append(property(data[word]["properties"][i][0],
                                            driver_state(data[word]["properties"][i][1][0],
                                                         data[word]["properties"][i][1][1],
                                                         data[word]["properties"][i][1][2],
                                                         data[word]["properties"][i][1][3],
                                                         data[word]["properties"][i][1][4],
                                                         data[word]["properties"][i][1][5],
                                                         data[word]["properties"][i][1][6],
                                                         ), data[word]["properties"][i][2]))
        milist = data[word]["mi_list"]
        tags=data[word]["tags"]
    return object(value_driver,property_driver,tags,word,mi_list=milist)


#function which checks wt are the tags which matches b/w an act and obj ... input takes the class rather than the name
def tag_match(act,obj):
    """

     description: checks what are the tags which matchches between and action and object
     parameter: act(actions class ), obj(objects class)
     returns: A list of matched tags

     """
    bla = []
    for i in range(len(obj.tag)):
        for j in range(len(act.tag)):
            if obj.tag[i]==act.tag[j][0]:
                bla.append(act.tag[j][1])
    return bla

#dtm - driver tag match list
def act_driver_state(dtm):



    asd=[0,0,0,0,0,0,0]
    for i in range (len(dtm)):
       for j in range(5):
            asd[j]=asd[j]+dtm[i][j]

    return driver_state(asd[0], asd[1], asd[2], asd[3], asd[4], asd[5], asd[6])

#converts the matrix to driver state class
def matrix_to_ds(matrix):
    ds = driver_state(0, 0, 0, 0, 0, 0, 0)
    ds.aki = matrix[0]
    ds.asi = matrix[1]
    ds.lsi = matrix[2]
    ds.lti = matrix[3]
    ds.sto = matrix[4]
    ds.ski = matrix[5]
    ds.tlo = matrix[6]
    return ds

#this does all the shit in object part combines the driverstate and properties and shit
def object_obj(aon):
    describer = aon.split(sep="&desc:")
    aon = describer[0]
    tags_ = []
    for i in range(len(describer)):
        describer[i] = describer[i].replace(" ", '')
    if len(describer) > 1:
        describer = describer[1].split(sep= ',')
        with open('C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\describer.json') as f:
            data = json.load(f)
            for i in range(len(describer)):
                tags_.append(data[int(describer[i])])

    aon = aon.split(sep="&prop:")
    for i in range(len(aon)):
        aon[i] = aon[i].replace(" ", '')
    obj = object_extractor(aon[0])
    for j in range(len(tags_)):
        obj.tag.append(tags_[j])

    if len(aon) > 1:
        aon_property_value_matrix = aon[1].split(sep=',')
        for i in range(len(obj.property)):
            obj.property[i].value = float(aon_property_value_matrix[i])
    return obj

#action ds function returns driiverstate of action and object
def action_ds(act,obj):
    driver_tag_match = tag_match(act, obj)
    driver = add_driver_state([act_driver_state(driver_tag_match) , act.ds, object_preference(obj.to_ds(),act.ods_preference_matrix)])
    return driver

#obj preference matrix idek wt this does... ohh yeah it multiplies the driverstate with preference matrix
def object_preference(obds,obds_pm):
    ahh = driver_state(0, 0, 0, 0, 0, 0, 0)
    ahh.aki = obds.aki * obds_pm.aki
    ahh.asi = obds.asi * obds_pm.asi
    ahh.lsi = obds.lsi * obds_pm.lsi
    ahh.lti = obds.lti * obds_pm.lti
    ahh.sto = obds.sto * obds_pm.sto
    ahh.ski = obds.ski * obds_pm.ski
    ahh.tlo = obds.tlo * obds_pm.tlo
    return ahh


########################################################################################################################

#function to add two driverstate
def add_driver_state(a):
    c = driver_state(0, 0, 0, 0, 0, 0, 0)
    for i in range(len(a)):
        c.aki = c.aki + a[i].aki
        c.asi = c.asi + a[i].asi
        c.lsi = c.lsi + a[i].lsi
        c.lti = c.lti + a[i].lti
        c.sto = c.sto + a[i].sto
        c.ski = c.ski + a[i].ski
        c.lto = c.tlo + a[i].tlo
    return c

#this takes the decision and converts to drivers IG
def derites_decision(decisionn):
    akii = derites(aki, decisionn.driver_state.aki)
    asii = derites(asi, decisionn.driver_state.asi)
    lsii = derites(lsi, decisionn.driver_state.lsi)
    ltii = derites(lti, decisionn.driver_state.lti)
    stoo = derites(sto, decisionn.driver_state.sto)
    stoo = derites(ski, decisionn.driver_state.ski)
    stoo = derites(tlo, decisionn.driver_state.tlo)
    return (akii+asii+lsii+ltii+stoo)

#yeah the final fuking function which returns final dec from decsion list
def make_dec(dec):
  decision_index=0
  for i in range(len(dec)):
      dec[i].derites = derites_decision(dec[i])
      if dec[i].derites>dec[decision_index].derites:
          decision_index = i

  return dec[decision_index]


def store(o,d=None,p=None,a=None):

  #opening the json file
  with open('C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\memory_asi.json') as f:
        m = json.load(f)
  #doin shit
  try:
    m['kaerve'][o]["self"] .append(time.time())
  except:
     try:
        m["kaerve"][o]={"self":[time.time()]}
     except:
         m["kaerve"]={}
         m["kaerve"][o]={"self":[time.time()]}
  if d!=None:
      try:
          m['kaerve'][o]['describer'][d].append(time.time())
      except:
          try:
            m['kaerve'][o]["describer"][d]=[time.time()]
          except:
            m['kaerve'][o]['describer']={}
            m['kaerve'][o]["describer"][d] = [time.time()]
  if p!=None:
      try:
          m['kaerve'][o]['property'][p].append(time.time())
      except:
          try:
            m['kaerve'][o]["property"][p]=[time.time()]
          except:
            m['kaerve'][o]['property']={}
            m['kaerve'][o]["property"][p] = [time.time()]



  if a!=None:
      try:
          m[a][o]["self"].append(time.time())
      except:
          try:
              m[a][o] = {"self": [time.time()]}
          except:
              m[a] = {}
              m[a][o] = {"self": [time.time()]}
      if d != None:
          try:
              m[a][o]['describer'][d].append(time.time())
          except:
              try:
                  m[a][o]["describer"][d] = [time.time()]
              except:
                  m[a][o]['describer'] = {}
                  m[a][o]["describer"][d] = [time.time()]
      if p != None:
          try:
              m[a][o]['property'][p].append(time.time())
          except:
              try:
                  m[a][o]["property"][p] = [time.time()]
              except:
                  m[a][o]['property'] = {}
                  m[a][o]["property"][p] = [time.time()]

  #storing back
  with open('C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\memory_asi.json', 'w') as j:
      json.dump(m, j, indent=4)


def clock(start_time):
    timer = time.time()- start_time
    return timer


def chunk_classifier(pos):
    x = int(pos.x)
    z = int(pos.z)
    h = 0
    if x >= 0 and z >= 0:
        h = 1
    elif x >= 0 >= z:
        h = 2
    elif x <= 0 <= z:
        h = 3
    elif x <= 0 and z <= 0:
        h = 4
    x = int(abs(x) / 100)
    z = int(abs(z) / 100)
    chunk = 4 * (0.5 * (x + z) * (x + z + 1) + z) + h
    return chunk

#this fuking function deletes the sim object from the world data
def delete(simobj):
    with open("C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\worldData.json") as f:
        wdata = json.load(f)
        wdata[simobj.chunk_no].pop(simobj.chunk_index)
    with open("C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\worldData.json","w") as j:
        json.dump(wdata,j)

def tlo(o,d=None,p=None,a=None,tloThres=40000012):
    ct = time.time()
    with open("C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\memory_asi.json") as f:
        mdata = json.load(f)
        tlodat=[]
        tlodat.append(mdata["kaerve"][o]['self'])
        if d!=None:
            tlodat.append(mdata["kaerve"][o]["describer"][d])
        if p!=None:
            tlodat.append(mdata["kaerve"][o]["property"][p])
        if a!=None:
            tlodat.append(mdata[a][o]["self"])
            tlodat.append(mdata[a][o]["describer"][d])
            tlodat.append(mdata[a][o]["property"][p])
    abtT=0
    for i in tlodat:
        for j in i:
            tempTime=ct-j
            if tempTime <=tloThres:
                abtT+=1

    print(abtT)

def perform(a,o=None):
    with open("C:\\Users\\akash\\PycharmProjects\\Demon\'s paradise\\demon-brain\\jsonFiles\\pinstrunctions.json") as f :
        pins=json.load(f)
        pinstruction = pins[a]
        print(pinstruction)
        print(type(pinstruction))
        if bool(int(pinstruction[0])):
            print(f'deleting {o.object.name}')
            delete(o)
    pass

def excecute(input,instruction=None):
    instruction = instruction.replace(' ','')
    instruction = instruction.split('&i:')
    flagi=True
    while flagi:
        for i in instruction:
            if i=='q':
                flagi=False
            #yennt - count panrathuku
            if i.startswith('yennt'):
                output = len(input)
                input=output
            #filod- oru certain object ah pirichi yedukurathu
            if i.startswith('filod'):
                output=[]
                temp=i.split('&obj:')
                temp=temp[1]
                try:
                    ptag=temp.split('&ptag:')
                    obj=ptag[0]
                    ptag=ptag[1]
                except:
                    ptag='111'
                    obj=temp
                try:
                    inputa = obj.split('&prop:')
                    object = inputa[0]
                    try:
                        inputb = inputa[1].split('&desc:')
                        property = inputb[0]
                        describer = inputb[1]
                    except:
                        property = inputa[1]
                        describer = None
                except:
                    property = None
                    try:
                        inputc = obj.split('&desc:')
                        object = inputc[0]
                        describer = inputc[1]

                    except:
                        object = obj

                for j in input:
                    boolfilod=False

                    #separating shit
                    try:
                        inputaj = j.object.name.split('&prop:')
                        objectj = inputaj[0]
                        try:
                            inputbj = inputaj[1].split('&desc:')
                            propertyj = inputbj[0]
                            describerj = inputbj[1]
                        except:
                            propertyj = inputaj[1]
                            describerj = None
                    except:
                        propertyj = None
                        try:
                            inputcj = j.object.name.split('&desc:')
                            objectj = inputcj[0]
                            describerj = inputcj[1]

                        except:
                            objectj = j.object.name


                    #ptag for object ps. ptag means preference tag
                    if ptag[0]=='1':
                        #object
                        if object==objectj:
                            boolfilod=True
                        else:
                            boolfilod=False
                    if ptag[1]=='1':
                        #property

                        if property==propertyj:
                            boolfilod=True
                        else:
                            boolfilod=False

                    if ptag[2]=='1':
                        #tag

                        if describer == describerj:
                            boolfilod=True
                        else:
                            boolfilod=False


                    if boolfilod:
                        output.append(j)
                input=output

    return output





#fuck u akash for making this shit and thanks for nothing nobody understood any fuking thing