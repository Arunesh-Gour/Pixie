class Fan:
   def __init__ (self):
      self.power = False
      self.speed = 0
      self.maxspeed = 3
   
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
      elif (key == "speed"):
         if (value):
            self.speed = value
         else:
            return -1
      elif (key == "speed-"):
         if (self.speed > 0):
            self.speed -= 1
         else:
            return -1
      elif (key == "speed+"):
         if (self.speed < self.maxspeed):
            self.speed += 1
         else:
            return -1
      else:
         return -1
      
      return 0
