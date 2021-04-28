class Room:
   def __init__ (self):
      self.name = None
      self.roomid = None
      self.appliances = []
   
   def signal (self, key, value=None):
      if (key == "keys?"):
         return ("name?", "roomid?", )
      elif (key == "name?"):
         return self.name
      elif (key == "name"):
         if (value):
            self.name = value
         else:
            return -1
      elif (key == "roomid?"):
         return self.roomid
      elif (key == "roomid"):
         if (value):
            self.roomid = value
         else:
            return -1
      elif (key == "appliances?"):
         return self.appliances
      elif (key == "appliances+"):
         if (value):
            self.appliances.append(value)
         else:
            return -1
      elif (key == "appliances"):
         if (value):
            self.appliances = value
         else:
            return -1
      else:
         return -1
      
      return 0
