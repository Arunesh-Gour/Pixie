class TV:
   def __init__ (self):
      self.power = False
      self.volume = 0
      self.maxvolume = 100
      self.channel = 0
      self.maxchannel = 999
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
      elif (key == "volume"):
         if (value):
            self.volume = value
         else:
            return -1
      elif (key == "volume-"):
         if (self.volume > 0):
            self.volume -= 1
         else:
            return -1
      elif (key == "volume+"):
         if (self.volume < self.maxvolume):
            self.volume += 1
         else:
            return -1
      elif (key == "channel"):
         if (value):
            self.channel = value
         else:
            return -1
      elif (key == "channel-"):
         if (self.channel > 0):
            self.channel -= 1
         else:
            return -1
      elif (key == "channel+"):
         if (self.channel < self.maxchannel):
            self.channel += 1
         else:
            return -1
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
