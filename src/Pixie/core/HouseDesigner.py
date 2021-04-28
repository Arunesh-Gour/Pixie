import random
import re

from ..models import (Door, Fan, House, Light, Room, TV,)

class HouseDesigner:
   def __init__ (self):
      self.house = None
      self.availablemodels = {
         "Door" : Door.Door,
         "Fan" : Fan.Fan,
         "House" : House.House,
         "Light" : Light.Light,
         "Room" : Room.Room,
         "TV" : TV.TV,
      }
      self.roomids = 1
   
   def getinput (self, namefor):
      name = str(\
         input("Name for your {0} (exclude '| @ % & : ; ='): ".format(\
            namefor, \
         ))\
      )
      if (len(re.findall("([|@%&:;=])", name)) > 0):
         print ("'| @ % & : ; =' characters are not allowed!")
         return False
      
      if (not (len(name) > 0)):
         print ("Please enter at-least 1 character for name")
         return False
      
      return name
   
   def create_interactive (self):
      self.createhouse()
      print("\n" + "="*36, "ROOMS", "="*36)
      rooms = []
      for _ in range(0, int(input("Total rooms (number): "))):
         room = self.createroom()
         print("\n" + "-"*33, "APPLIANCES", "-"*34)
         appliances = []
         for __ in range(0, int(input(\
            "Total appliances in room '{0}' (number): ".format(\
               room.name
            )\
            ))):
            appliances.append(self.createappliance())
         print("-"*79)
         
         room.roomid = self.roomids
         self.roomids += 1
         room.signal("appliances", appliances)
         rooms.append(room)
         print("\n")
      
      print("="*79 + "\n")
      self.house.availableroomid = self.roomids
      self.house.signal("rooms", rooms)
      
      return 0
   
   def createhouse (self):
      self.house = self.availablemodels["House"]()
      print("\n" + "*"*36, "HOUSE", "*"*36 + "\n")
      name = False
      while (name == False):
         name = self.getinput("house")
      
      self.house.signal("name", name)
      
      return 0
   
   def createroom (self):
      room = self.availablemodels["Room"]()
      name = False
      while (name == False):
         name = self.getinput("room")
      
      room.signal("name", name)
      return room
   
   def createappliance (self):
      name = False
      while (name == False):
         name = self.getinput("appliance type {0}".format(\
            ("Door", "Fan", "Light", "TV"), \
         ))
         if (name not in ("Door", "Fan", "Light", "TV",)):
            name = False
            print("Invalid appliance type!")
      appliance = self.availablemodels[name]()
      if (name == "Door"):
         appliance.signal("power", random.choice((True, False,)))
         appliance.signal("secured", random.choice((True, False,)))
      elif (name == "Fan"):
         appliance.signal("power", random.choice((True, False,)))
         appliance.signal("speed", random.randint(0, appliance.maxspeed))
      elif (name == "Light"):
         appliance.signal("power", random.choice((True, False,)))
         appliance.signal("brightness", random.randint(\
            0, appliance.maxbrightness\
         ))
      elif (name == "TV"):
         appliance.signal("power", random.choice((True, False,)))
         appliance.signal("volume", random.randint(\
            0, appliance.maxvolume\
         ))
         appliance.signal("channel", random.randint(\
            0, appliance.maxchannel\
         ))
         appliance.signal("brightness", random.randint(\
            0, appliance.maxbrightness\
         ))
      return appliance
# Guard line - 79th character at end (length = 79):
# -----------------------------------------------------------------------------
