#ask user where should i look?
print("Where should i look")
place = input()
#in the bedroom
#under the bed: found some socks but not battery
#anything else: found some mess but no battery
if (place == "in the bedroom"):
  print("Where is the bedroom?")
  bedroom_place = input()
 if (bedroom_place == "under the bed"):
  print("Found some socks but no battery!")
 else:
  print("Found some mess but no battery!")

#in the bathroom
#in the bathtub: found a rubber duck but no battery
#something else: its wet but there is no battery
bathroom_place = input()
if(bathroom_place == "in the bathtub"):
  print("Found a rubber duck but no battery!")
 else:
  print("Its wet but there is no battery!")

#in the lab:
#on the table: found the battery!
#something else: found some tools but no battery
#anything else: don't know where that is, but i will keep looking
lab_place = input()
if (lab_place == "on the table"):
  print("Found the battery")
 elif:
   print("Found some tools but no battery")
 else:
   print("Dont know where that is, but i will keep looking")
