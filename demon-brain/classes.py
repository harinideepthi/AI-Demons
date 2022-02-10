#decision class
class decision:
    def __init__(self, driverState, sentence, derites):
        self.driverState = driverState
        self.sentence = sentence
        self.derites = derites

#akash sentence notation ... fuck I never used this
class asn:
    def __init__(self, subject,object,verb):
        self.subject = subject
        self.object = object
        self.verb = verb


#driver class ... like defining aki itself /asi itslef wt ever man u get it
class driver:
    def __init__(self, le, ue, pi1, pi2, pi3):
        self.le = le
        self.ue = ue
        self.pi1 = pi1
        self.pi2 = pi2
        self.pi3 = pi3

#driver state is the collection of all the fuking drivers
class driverState:
    def __init__(self, aki, asi, lti, lsi, sto, ski,tlo):
        self.aki = aki
        self.asi = asi
        self.lti = lti
        self.lsi = lsi
        self.sto = sto
        self.ski = ski
        self.tlo = tlo
    #print method to print the driverstate
    def print(self):
        print('aki:' + str(self.aki))
        print('asi:' + str(self.asi))
        print('lsi:' + str(self.lsi))
        print('lti:' + str(self.lti))
        print('sto:' + str(self.sto))
        print('ski:' + str(self.ski))
        print('tlo:' + str(self.tlo))

#property class ... yeah the property which defines the object thing
class property:
    def __init__(self, value, dm_matrix, name):
        self.value = value
        self.dm_matrix = dm_matrix
        self.name = name

#object thing .. uk wt an object is ... object man subject object action
class object:
    def __init__(self, driver_state, property, tag,name,mi_list):
        self.driver_state = driver_state
        self.property = property
        self.tag = tag
        self.name = name
        self.mi_list = mi_list
    #methon which converts the object into a driverstate
    def to_ds(self):
        temp = driverState(0, 0, 0, 0, 0, 0, 0)
        # calculating driver values for properties
        for i in range(len(self.property)):
            temp.aki = temp.aki + self.property[i].value * self.property[i].dm_matrix.aki
            temp.asi = temp.asi + self.property[i].value * self.property[i].dm_matrix.asi
            temp.lti = temp.lti + self.property[i].value * self.property[i].dm_matrix.lti
            temp.lsi = temp.lsi + self.property[i].value * self.property[i].dm_matrix.lsi
            temp.sto = temp.sto + self.property[i].value * self.property[i].dm_matrix.sto
        # adding inbuilt driver values with property driver values
        temp.aki = temp.aki + self.driver_state.aki
        temp.asi = temp.asi + self.driver_state.asi
        temp.lti = temp.lti + self.driver_state.lti
        temp.lsi = temp.lsi + self.driver_state.lsi
        temp.sto = temp.sto + self.driver_state.sto
        temp.ski = temp.ski + self.driver_state.ski
        temp.tlo = temp.tlo + self.driver_state.tlo

        return temp

#action class nothing much to explain
class action:
    def __init__(self,tag,ds,ods_preference_matrix,name,mi_list):
        self.tag = tag
        self.ds = ds
        self.ods_preference_matrix = ods_preference_matrix
        self.name = name
        self.mi_list = mi_list

#creating a special class for the simulation
class SimObject:
    def __init__(self,object , obj_id, pos,chunk_no,chunk_index):
        self.object = object
        self.id = obj_id
        self.pos = pos
        self.chunk_no = chunk_no
        self.chunk_index = chunk_index

    def translate(self, pos):
        self.pos = pos


