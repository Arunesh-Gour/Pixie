class House:
   def __init__ (self):
      self.name = None
      self.availableroomid = 1
      self.rooms = []
   
   def signal (self, key, value=None):
      if (key == "keys?"):
         return ("name?", "availableroomid?",)
      elif (key == "name?"):
         return self.name
      elif (key == "name"):
         if (value):
            self.name = value
         else:
            return -1
      elif (key == "availableroomid?"):
         return self.availableroomid
      elif (key == "availableroomid"):
         if (value):
            self.availableroomid = value
         else:
            return -1
      elif (key == "rooms?"):
         return self.rooms
      elif (key == "rooms+"):
         if (value):
            self.rooms.append(value)
         else:
            return -1
      elif (key == "rooms"):
         if (value):
            self.rooms = value
         else:
            return -1
      else:
         return -1
      
      return 0
