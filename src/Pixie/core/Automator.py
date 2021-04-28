import os
import time
import threading
import multiprocessing

from ..db import dbController
from . import (AutoExecutor, HouseDesigner, PersonController,)
# from .AutoExecutor import AutoExecutor

currentsystemos = 0
# 0:linux, 1:windows
# "linux": ("linux", "windows")
systemoscommands = {\
   "clear" : ("clear", "cls",), \
}

def sysrun (command):
   global currentsystemos, systemoscommands
   try:
      os.system(systemoscommands[command][currentsystemos])
   except Exception as e:
      return -1
   return 0

class Automator:
   def __init__ (self):
      self.house = None
      self.timespeed = 60 # 1 minute => 1 sec.
      self.dbController = dbController.DBController()
      
      if (self.dbController.load() != 0):
         sysrun("clear")
         housedesigner = HouseDesigner.HouseDesigner()
         housedesigner.create_interactive()
         self.house = housedesigner.house
         self.dbController.house = self.house
         if (self.dbController.save() != 0):
            return -1
         sysrun("clear")
      else:
         self.house = self.dbController.house
      
      # pc = personController; used short to reduce variables to pc.person.*
      self.pc = PersonController.PersonController(self.house)
      self.pc.speed = self.timespeed
      
      self.dbControllerExecutor = AutoExecutor.AutoExecutor()
      self.pcExecutor = AutoExecutor.AutoExecutor()
      self.statusExecutor = AutoExecutor.AutoExecutor()
      self.doorExecutor = AutoExecutor.AutoExecutor()
      self.fanExecutor = AutoExecutor.AutoExecutor()
      self.lightExecutor = AutoExecutor.AutoExecutor()
      self.tvExecutor = AutoExecutor.AutoExecutor()
      
      self.dbControllerController = None
      self.pcController = None
      self.statusController = None
      self.doorController = None
      self.fanController = None
      self.lightController = None
      self.tvController = None
      
      self.personstates = (\
         "sleeping", \
         "half awake", \
         "awake", \
         "cautious", \
      )
      self.personpositions = (\
         "laying down", \
         "sitting", \
         "standing", \
         "walking", \
         "jogging", \
         "running", \
      )
   
   def __del__ (self):
      self.kill()
      self.dbController.house = self.house
      if (self.dbController.save() != 0):
         return -1
      return 0
   
   # def auto_exec (self, exec_function, interval=60):
   
   def automate (self):
      self.dbControllerController = multiprocessing.Process(\
         target=self.dbControllerExecutor.auto_execute, \
         args=(self.auto_dbsave, None, 660, self.timespeed,), \
         daemon=True, \
      )
      self.pcController = multiprocessing.Process(\
         target=self.pcExecutor.auto_execute, \
         args=(self.pc.change_automatic, None, 60, self.timespeed,), \
      )
      self.statusController = threading.Thread(\
         target=self.statusExecutor.auto_execute, \
         args=(self.status, None, 60, self.timespeed,), \
         daemon=True, \
      )
      self.doorController = threading.Thread(\
         target=self.doorExecutor.auto_execute, \
         args=(self.control_door, None, 600, self.timespeed,), \
         daemon=True, \
      )
      self.fanController = threading.Thread(\
         target=self.fanExecutor.auto_execute, \
         args=(self.control_fan, None, 300, self.timespeed,), \
         daemon=True, \
      )
      self.lightController = threading.Thread(\
         target=self.lightExecutor.auto_execute, \
         args=(self.control_light, None, 180, self.timespeed,), \
         daemon=True, \
      )
      self.tvController = threading.Thread(\
         target=self.tvExecutor.auto_execute, \
         args=(self.control_tv, None, 120, self.timespeed,), \
         daemon=True, \
      )
      
      self.dbControllerController.start()
      self.pcController.start()
      self.statusController.start()
      self.doorController.start()
      self.fanController.start()
      self.lightController.start()
      self.tvController.start()
      
      self.doorController.join()
      self.fanController.join()
      self.lightController.join()
      self.tvController.join()
      self.statusController.join()
      self.pcController.join()
      self.dbControllerController.join()
      
      return 0
   
   def kill (self):
      self.doorExecutor.kill()
      self.fanExecutor.kill()
      self.lightExecutor.kill()
      self.tvExecutor.kill()
      self.statusExecutor.kill()
      self.pcExecutor.kill()
      self.dbControllerExecutor.kill()
      return 0
   
   def auto_dbsave (self):
      self.dbController.house = self.house
      if (self.dbController.save()):
         return -1
      return 0
   
   def status (self):
      sysrun("clear")
      if (self.pc.person.location == 0):
         print(\
            "PERSON:\n" \
            + "Location: Not in home.\n" \
            + "State: N/A.\n" \
            + "Position: N/A.\n" \
         )
      elif (self.pc.person.location > 0):
         print(\
            "PERSON:\n" \
            + "Location: {0}.\n".format(\
               (self.house.rooms[self.pc.person.location].name + " room")\
            ) \
            + "State: {0}.\n".format(\
               self.personstates[self.pc.person.location]\
            ) \
            + "Position: {0}.\n".format(\
               self.personpositions[self.pc.person.position]\
            ) \
         )
      print("HOUSE:")
      for room in self.house.rooms:
         print(room.name + " room: ", end='')
         appliance_done = 0
         space_width = len(room.name) + 7
         for appliance in room.appliances:
            if (appliance_done >= 2):
               print("\n" + " "*space_width, end='')
            if (type(appliance).__name__ == 'Door'):
               print("Door (powered {0}, {1}), ".format(\
                     (\
                        "on" if (appliance.signal("power?") == True) \
                        else "off"\
                     ), \
                     (\
                        "locked" if (appliance.signal("secured?") == True) \
                        else "unlocked"\
                     ), \
                  ), \
                  end='', \
               )
            elif (type(appliance).__name__ == 'Fan'):
               print("Fan (powered {0}, speed={1}), ".format(\
                     (\
                        "on" if (appliance.signal("power?") == True) \
                        else "off"\
                     ), \
                     (appliance.signal("speed?")), \
                  ), \
                  end='', \
               )
            elif (type(appliance).__name__ == 'Light'):
               print("Light (powered {0}, brightness={1}), ".format(\
                     (\
                        "on" if (appliance.signal("power?") == True) \
                        else "off"\
                     ), \
                     (appliance.signal("brightness?")), \
                  ), \
                  end='', \
               )
            elif (type(appliance).__name__ == 'TV'):
               print("TV (powered {0}, volume={1}, channel={2}, brightness={3}), ".format(\
                     (\
                        "on" if (appliance.signal("power?") == True) \
                        else "off"\
                     ), \
                     (appliance.signal("volume?")), \
                     (appliance.signal("channel?")), \
                     (appliance.signal("brightness?")), \
                  ), \
                  end='', \
               )
            appliance_done += 1
         print("\n", end='')
      print("\n", end='')
      return 0
   
   def control_door (self):
      if (self.pc.person.location == 0):
         for room in self.house.rooms:
            for appliance in room.appliances:
               if ((type(appliance).__name__ == "Door") and \
                  (appliance.signal("power?") == True) and \
                  (appliance.signal("secured?") == False)):
                  appliance.signal("lock")
      elif (self.pc.person.location > 0):
         if (self.pc.person.state < 2):
            for room in self.house.rooms:
               for appliance in room.appliances:
                  if ((type(appliance).__name__ == "Door") and \
                     (appliance.signal("power?") == True) and \
                     (appliance.signal("secured?") == False)):
                     appliance.signal("lock")
      return 0
   
   def control_fan (self):
      if (self.pc.person.location == 0):
         for room in self.house.rooms:
            for appliance in room.appliances:
               if ((type(appliance).__name__ == "Fan") and \
                  (appliance.signal("power?") == True)):
                  appliance.signal("power-")
      elif (self.pc.person.location > 0):
         for room in self.house.rooms:
            if (self.pc.person.location != room.roomid):
               for appliance in room.appliances:
                  if ((type(appliance).__name__ == "Fan") and \
                     (appliance.signal("power?") == True)):
                     appliance.signal("power-")
            elif (self.pc.person.location == room.roomid):
               if (self.pc.person.state < 2):
                  for appliance in room.appliances:
                     if ((type(appliance).__name__ == "Fan") and \
                        (appliance.signal("power?") == False)):
                        appliance.signal("power+")
                        if (appliance.signal("speed?") == appliance.maxspeed):
                           appliance.signal("speed-")
      return 0
   
   def control_light (self):
      if (self.pc.person.location == 0):
         for room in self.house.rooms:
            for appliance in room.appliances:
               if ((type(appliance).__name__ == "Light") and \
                  (appliance.signal("power?") == True)):
                  appliance.signal("power-")
      elif (self.pc.person.location > 0):
         for room in self.house.rooms:
            if (self.pc.person.location != room.roomid):
               for appliance in room.appliances:
                  if ((type(appliance).__name__ == "Light") and \
                     (appliance.signal("power?") == True)):
                     appliance.signal("power-")
            elif (self.pc.person.location == room.roomid):
               if (self.pc.person.state < 2):
                  for appliance in room.appliances:
                     if ((type(appliance).__name__ == "Light") and \
                        (appliance.signal("power?") == True)):
                        if (self.pc.person.state == 0):
                           appliance.signal("power-")
                        elif (self.pc.person.state == 1):
                           if (appliance.signal("brightness?") \
                              >= int(appliance.maxbrightness/2)):
                              appliance.signal(\
                                 "brightness", int(appliance.brightness/2)\
                              )
      return 0
   
   def control_tv (self):
      if (self.pc.person.location == 0):
         for room in self.house.rooms:
            for appliance in room.appliances:
               if ((type(appliance).__name__ == "TV") and \
                  (appliance.signal("power?") == True)):
                  appliance.signal("power-")
      elif (self.pc.person.location > 0):
         for room in self.house.rooms:
            if (self.pc.person.location != room.roomid):
               for appliance in room.appliances:
                  if ((type(appliance).__name__ == "TV") and \
                     (appliance.signal("power?") == True)):
                     appliance.signal("power-")
            elif (self.pc.person.location == room.roomid):
               if (self.pc.person.state < 2):
                  for appliance in room.appliances:
                     if ((type(appliance).__name__ == "TV") and \
                        (appliance.signal("power?") == True)):
                        if (self.pc.person.state == 0):
                           appliance.signal("power-")
                        elif (self.pc.person.state == 1):
                           if (appliance.signal("volume?") \
                              >= int(appliance.maxvolume/2)):
                              appliance.signal(\
                                 "volume", int(appliance.volume * (3/4))\
                              )
                           elif (appliance.signal("brightness?") \
                              >= int(appliance.maxbrightness/2)):
                              appliance.signal(\
                                 "brightness", \
                                 int(appliance.brightness * (3/4)), \
                              )
      return 0
# Guard line - 79th character at end (length = 79):
# -----------------------------------------------------------------------------
