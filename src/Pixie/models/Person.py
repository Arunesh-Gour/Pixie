class Person:
   def __init__ (self):
      self.state = 0
      self.position = 0
      self.location = 0
      """
         states
         ------
            0 - sleeping
            1 - halfawake
            2 - awake
            3 - cautious
         
         position
         --------
            0 - laying down
            1 - sitting
            2 - standing
            3 - walking
            4 - jogging
            5 - running
         
         location
         --------
            0 - outside
            [1:] - locations
      """
   
   def signal (self, key, value=None):
      if (key == "keys?"):
         return ("state?", "position?", "location?", )
      elif (key == "state?"):
         return self.state
      elif (key == "state"):
         if (value):
            self.state = value
         else:
            return -1
      elif (key == "position?"):
         return self.position
      elif (key == "position"):
         if (value):
            self.position = value
         else:
            return -1
      elif (key == "location?"):
         return self.location
      elif (key == "location"):
         if (value):
            self.location = value
         else:
            return -1
      else:
         return -1
      
      return 0
