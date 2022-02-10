import json
import random
from classes import *
from functions import *
from character import *
decisions=[]
private_channel = []
#terminal
def terminal():
    global decisions
    flag = True

    while flag:
      cmd = input('>>>')
      cmd = cmd.lower()
      if cmd in  ['stop','quit','exit']:
        flag = False

      if cmd in ['object','obj','o']:
            aon = input('input object here: ')
            object_driver_state = objectExtractor(aon).to_ds()
            print(derites(aki,object_driver_state.aki))


      if cmd in ['action','act','a']:
            objj = input('enter the object: ')
            actt = input('input action here: ')
            driver = actionDs(action_extractor(actt), objectExtractor(objj))
            driver.print()

      if cmd in ['decision','dec']:
            ooo = input('enter the object: ')
            aaa = input('enter the action: ')
            dec_ds = actionDs(action_extractor(aaa), objectExtractor(ooo))
            decisions.append(decision(dec_ds,aaa+' '+ooo,0))

      if cmd in ['print_decision','print_dn']:
          for i in range(len(decisions)):
              print(decisions[i].sentence)
              decisions[i].driverState.print()

      if cmd in ['pop_decision','pop_dn']:
          decisions.pop()

      if cmd in ['delete_decision','delete_dn']:
          j = input('index to delete: ')
          del(decisions[int(j)-1])

      if cmd in ['delete_all_decisions']:
          decisions =[]

      if cmd == 'help':
          print('prints help')

      if cmd in ['make_decision', 'mkdn' ,'make_dn','mk_dn']:
          final_decision = makeDec(decisions)
          print(final_decision.sentence)
          final_decision.driverState.print()