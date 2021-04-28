class Fan:
   def __init__ (self):
      self.power = False
      self.speed = 0
      self.maxspeed = 3
   
   def signal(self, key, value=None):
      if (key == "keys?"):
         return ("power?", "speed?", )
      elif (key == "power?"):
         return self.power
      elif (key == "speed?"):
         return self.speed
      elif (key == "power"):
         if (value):
            self.power = value
         else:
            return -1
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
