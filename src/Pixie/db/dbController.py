from ..models import House
from . import dbConnector

class DBController:
   def __init__ (self):
      self.house = House.House()
      self.dbConnector = dbConnector.DBConnector()
      
      self.filewpath = "./Pixie/db/storagefile.txt"
   
   def signal (self, key, value=None):
      if (key == "house?"):
         return self.house
      elif (key == "house"):
         if (value):
            self.house = value
         else:
            return -1
      else:
         return -1
      
      return 0
   
   def save (self):
      self.dbConnector.signal("house", self.house)
      self.dbConnector.signal("filewpath", self.filewpath)
      if (self.dbConnector.save() != 0):
         return -1
      
      return 0
   
   def load (self):
      self.dbConnector.signal("filewpath", self.filewpath)
      if (self.dbConnector.load() != 0):
         return -1
      
      self.house = self.dbConnector.signal("house?")
      
      return 0
