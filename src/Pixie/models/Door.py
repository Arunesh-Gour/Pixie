class Door:
   def __init__ (self):
      self.power = False
      self.secured = True
   
   def signal(self, key, value=None):
      if (key == "keys?"):
         return ("power?", "secured?", )
      elif (key == "power?"):
         return self.power
      elif (key == "secured?"):
         return self.secured
      elif (key == "power"):
         if (value):
            self.power = value
         else:
            return -1
      elif (key == "power+"):
         self.power = True
      elif (key == "power-"):
         self.power = False
      elif (key == "lock"):
         self.secured = True
      elif (key == "unlock"):
         self.secured = False
      elif (key == "secured"):
         if (value):
            self.secured = value
         else:
            return -1
      else:
         return -1
      
      return 0
