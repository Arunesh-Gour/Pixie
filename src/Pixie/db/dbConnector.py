import os
import re

from ..models import (Door, Fan, House, Light, Room, TV,)

def convert_to_bool (string):
   if (string == "True"):
      return True
   elif (string == "False"):
      return False
   else:
      raise ValueError("convert_to_bool: " \
         + "unrecognized bool string '{0}'".format(string))

class DBConnector:
   def __init__ (self):
      self.house = None
      self.filewpath = None
      self.availablemodels = {
         "Door" : Door.Door,
         "Fan" : Fan.Fan,
         "House" : House.House,
         "Light" : Light.Light,
         "Room" : Room.Room,
         "TV" : TV.TV,
      }
      self.availablevaluetypes = {
         "int" : int,
         "str" : str,
         "bool" : convert_to_bool,
      }
   
   def signal (self, key, value=None):
      if (key == "house?"):
         return self.house
      elif (key == "filewpath?"):
         return self.filewpath
      elif (key == "house"):
         if (value):
            self.house = value
         else:
            return -1
      elif (key == "filewpath"):
         if (value):
            self.filewpath = value
         else:
            return -1
      else:
         return -1
      
      return 0
   
   def save (self):
      housestring = "|"
      housestring += "@{0}@".format(str(type(self.house).__name__))
      for ikey in self.house.signal("keys?"):
         housestring += "@{0}={1}@".format(\
            str(type(self.house.signal(ikey)).__name__), \
            str(self.house.signal(ikey)), \
         )
      
      roomstring = ""
      for room in self.house.signal("rooms?"):
         croomstring = "%"
         croomstring += "&{0}&".format(str(type(room).__name__))
         for ikey in room.signal("keys?"):
            croomstring += "&{0}={1}&".format(\
               str(type(room.signal(ikey)).__name__), \
               str(room.signal(ikey)), \
            )
         
         appliancestring = ""
         for appliance in room.signal("appliances?"):
            cappliancestring = ":"
            cappliancestring += ";{0};".format(str(type(appliance).__name__))
            for ikey in appliance.signal("keys?"):
               cappliancestring += ";{0}={1};".format(\
                  str(type(appliance.signal(ikey)).__name__), \
                  str(appliance.signal(ikey)), \
               )
            cappliancestring += ":"
            appliancestring += cappliancestring
         
         croomstring += appliancestring
         
         croomstring += "%"
         roomstring += croomstring
      
      housestring += roomstring
      
      housestring += "|"
      
      if (not (os.path.exists(self.filewpath))):
         os.system(">> " + self.filewpath)
      
      with open(self.filewpath, "w") as filehandler:
         filehandler.write(housestring)
      
      return 0
   
   def load (self):
      if (not (os.path.exists(self.filewpath))):
         return -1
      
      storedstring = None
      with open(self.filewpath, "r") as filehandler:
         storedstring = str(filehandler.read())
      
      houses = [house \
         for house in re.split("\|", storedstring.strip()) \
         if (house != None and house != '') \
      ]
      
      housescollection = []
      #housescollection = None
      for house in houses:
         houseattribs = [houseattrib \
            for houseattrib in re.split("@", str(house)) \
            if (houseattrib != None and houseattrib != '') \
         ]
         
         modelhouse = self.availablemodels[str(houseattribs[0])]()
         
         for houseattrib, ikey in \
            zip(houseattribs[1:], modelhouse.signal("keys?")):
            modelhouse.signal(\
               key=str(ikey[:-1]), \
               value=self.availablevaluetypes[\
                  str(re.split("=", houseattrib, 1)[0])
               ](str(re.split("=", houseattrib, 1)[1])), \
            )
         
         rooms = [room \
            for room in re.split(\
               "%", \
               str(re.findall("\@(\%\&.*\%)", str(house))[0]), \
            ) \
            if (room != None and room != '') \
         ]
         
         roomscollection = []
         for room in rooms:
            roomattribs = [roomattrib \
               for roomattrib in re.split("&", str(room)) \
               if (roomattrib != None and roomattrib != '') \
            ]
            
            modelroom = self.availablemodels[str(roomattribs[0])]()
            
            for roomattrib, ikey in \
               zip(roomattribs[1:], modelroom.signal("keys?")):
               modelroom.signal(\
                  key=str(ikey[:-1]), \
                  value=self.availablevaluetypes[\
                     str(re.split("=", roomattrib, 1)[0])
                  ](str(re.split("=", roomattrib, 1)[1])), \
               )
            
            appliances = [appliance \
               for appliance in re.split(\
                  ":", \
                  str(re.findall("\&(\:\;.*\:)", str(room))[0]), \
               ) \
               if (appliance != None and appliance != '') \
            ]
            
            appliancescollection = []
            for appliance in appliances:
               applianceattribs = [applianceattrib \
                  for applianceattrib in re.split(";", str(appliance)) \
                  if (applianceattrib != None and applianceattrib != '') \
               ]
               
               modelappliance = self.availablemodels[str(applianceattribs[0])]()
               
               for applianceattrib, ikey in \
                  zip(applianceattribs[1:], modelappliance.signal("keys?")):
                  modelappliance.signal(\
                     key=str(ikey[:-1]), \
                     value=self.availablevaluetypes[\
                        str(re.split("=", applianceattrib, 1)[0])
                     ](str(re.split("=", applianceattrib, 1)[1])), \
                  )
               
               appliancescollection.append(modelappliance)
            
            modelroom.signal(key="appliances", value=appliancescollection)
            roomscollection.append(modelroom)
         
         modelhouse.signal(key="rooms", value=roomscollection)
         #housescollection = modelhouse
         housescollection.append(modelhouse)
      
      self.house = housescollection[0]
      
      return 0
# Guard line - 79th character at end (length = 79):
# -----------------------------------------------------------------------------
