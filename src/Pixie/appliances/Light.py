class Light:
   def __init__ (self):
      self.power = False
      self.brightness = 0
      self.maxbrightness = 100
   
   def signal(self, key, value=None):
      if (key == "power"):
         if (self.power):
            self.power = False
         else:
            self.power = True
      elif (key == "power+"):
         self.power = True
      elif (key == "power-"):
         self.power = False
      elif (key == "brightness"):
         if (value):
            self.brightness = value
         else:
            return -1
      elif (key == "brightness-"):
         if (self.brightness > 0):
            self.brightness -= 1
         else:
            return -1
      elif (key == "brightness+"):
         if (self.brightness < self.maxbrightness):
            self.brightness += 1
         else:
            return -1
      else:
         return -1
      
      return 0
