import random
import time
import threading

from ..models import (Person,)

class PersonController:
   def __init__ (self, house, person=None):
      self.house = house
      self.speed = 60 # 1 minute => 1 sec.
      self.lock = threading.Lock()
      self.killthread = False
      if (person):
         self.person = person
      else:
         self.person = Person.Person()
         self.person.state = random.randint(0, 2)
         if (self.person.state < 2):
            self.person.position = random.randint(0, 2)
         else:
            self.person.position = random.randint(1, 5)
         self.person.location = random.randint(1, self.house.availableroomid)
   
   def auto_check (self, variable, value):
      while (self.person.signal(variable) == value):
         if (self.killthread):
            time.sleep(5)
            self.killthread = False
            return
      
      self.killthread = True
      time.sleep(5)
      self.killthread = False
   
   def auto_function (self, efunction, time_length=60):
      markcount = 0
      while (markcount < time_length):
         time.sleep(1)
         markcount += (1 * self.speed)
         if (self.killthread):
            return
      
      self.lock.acquire()
      efunction()
      self.lock.release()
   
   def change_automatic (self):
      # Callable in thread
      # every x/y/z min/sec, change state/pos/loc, as necessary.
      self.killthread = False
      if (self.lock.locked()):
         self.lock.release()
      
      if (self.person.location == 0):
         t1 = threading.Thread(\
            target=self.auto_function, \
            args=(self.change_location, 1200,), \
            daemon=True, \
         )
         t1.start()
         t1.join()
      else:
         if (self.person.state == 0):
            t1 = threading.Thread(\
               target=self.auto_function, \
               args=(self.change_state, 600,), \
               daemon=True, \
            )
            t1.start()
            t1.join()
         elif (self.person.state == 1):
            tx = threading.Thread(\
               target=self.auto_check, \
               args=("state?", 1,), \
               daemon=True, \
            )
            tx.start()
            t1 = threading.Thread(\
               target=self.auto_function, \
               args=(self.change_state, 120,), \
               daemon=True, \
            )
            t1.start()
            t2 = threading.Thread(\
               target=self.auto_function, \
               args=(self.change_position, 60,), \
               daemon=True, \
            )
            t2.start()
            t2.join()
            del t2
            t2 = threading.Thread(\
               target=self.auto_function, \
               args=(self.change_position, 60,), \
               daemon=True, \
            )
            t2.start()
            t2.join()
            t1.join()
            self.killthread = True
         elif (self.person.state >= 2):
            if (self.person.position < 2):
               tx = threading.Thread(\
                  target=self.auto_check, \
                  args=("state?", self.person.state,), \
                  daemon=True, \
               )
               tx.start()
               ty = threading.Thread(\
                  target=self.auto_check, \
                  args=("position?", self.person.position,), \
                  daemon=True, \
               )
               ty.start()
               t1 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_state, 600,), \
                  daemon=True, \
               )
               t1.start()
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_position, 400,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_position, 400,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               t1.join()
               self.killthread = True
            elif (self.person.position == 2):
               tx = threading.Thread(\
                  target=self.auto_check, \
                  args=("state?", self.person.state,), \
                  daemon=True, \
               )
               tx.start()
               ty = threading.Thread(\
                  target=self.auto_check, \
                  args=("position?", 2,), \
                  daemon=True, \
               )
               ty.start()
               t1 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_state, 120,), \
                  daemon=True, \
               )
               t1.start()
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_position, 60,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_position, 60,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               t1.join()
               self.killthread = True
            elif (self.person.position > 2):
               tx = threading.Thread(\
                  target=self.auto_check, \
                  args=("state?", self.person.state,), \
                  daemon=True, \
               )
               tx.start()
               ty = threading.Thread(\
                  target=self.auto_check, \
                  args=("position?", self.person.position,), \
                  daemon=True, \
               )
               ty.start()
               t1 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_position, 60,), \
                  daemon=True, \
               )
               t1.start()
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_location, 10,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_location, 10,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_location, 10,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_location, 10,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_location, 10,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               del t2
               t2 = threading.Thread(\
                  target=self.auto_function, \
                  args=(self.change_location, 10,), \
                  daemon=True, \
               )
               t2.start()
               t2.join()
               t1.join()
               self.killthread = True
   
   def change_state (self, state_range=None):
      if (state_range):
         self.person.state = random.randint(state_range[0], state_range[1])
      else:
         if (self.person.state == 0):
            self.person.state = random.choice(\
               (\
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  1, 1, 1, 1, 1,
               )\
            )
         elif (self.person.state == 1):
            if (self.person.position == 0):
               self.person.state = random.choice(\
                  (\
                     0, 0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1,
                     2, 2,
                  )\
               )
            elif (self.person.position == 1):
               self.person.state = random.choice(\
                  (\
                     0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2,
                  )\
               )
            elif (self.person.position == 2):
               self.person.state = random.choice(\
                  (\
                     0, 0,
                     1, 1, 1, 
                     2, 2, 2, 2, 2, 2, 2, 2, 2,
                  )\
               )
         elif (self.person.state == 2):
            if (self.person.position == 0):
               self.person.state = random.choice(\
                  (\
                     0, 0, 0, 0, 0,
                     1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2,
                  )\
               )
            elif (self.person.position == 1):
               self.person.state = random.choice(\
                  (\
                     0, 0, 
                     1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2,
                  )\
               )
            elif (self.person.position == 2):
               self.person.state = random.choice(\
                  (\
                     0,
                     1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2,
                  )\
               )
            elif (self.person.position > 2):
               self.person.state = random.choice(\
                  (\
                     2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                     3,
                  )\
               )
         elif (self.person.state == 3):
            self.person.state = random.choice(\
               (\
                  0, 0, 0,
                  1,
                  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                  3, 3, 3, 3, 3, 3, 3
               )\
            )
      
      return 0
   
   def change_position (self, position_range=None):
      if (position_range):
         self.person.position = random.randint(position_range[0], position_range[1])
      else:
         if (self.person.state == 0):
            pass
         elif (self.person.state == 1):
            if (self.person.position == 0):
               self.person.position = random.choice(\
                  (\
                     0, 0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1,
                     2, 2,
                  )\
               )
            elif (self.person.position == 1):
               self.person.position = random.choice(\
                  (\
                     0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2,
                  )\
               )
            elif (self.person.position == 2):
               self.person.position = random.choice(\
                  (\
                     0, 0,
                     1, 1, 1, 
                     2, 2, 2, 2, 2, 2, 2, 2, 2,
                  )\
               )
         elif (self.person.state == 2):
            if (self.person.position == 0):
               self.person.position = random.choice(\
                  (\
                     0, 0,
                     1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2, 2, 2, 2,
                     3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                  )\
               )
            elif (self.person.position == 1):
               self.person.position = random.choice(\
                  (\
                     0,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2,
                     3, 3, 3, 3, 3, 3, 3, 3, 3,
                  )\
               )
            elif (self.person.position == 2):
               self.person.position = random.choice(\
                  (\
                     0,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     2, 2, 2, 2, 2, 2,
                     3, 3, 3, 3, 3, 3, 3, 3, 3,
                     4, 4, 4, 4,
                     5, 5,
                  )\
               )
            elif (self.person.position > 2):
               self.person.position = random.choice(\
                  (\
                     1,
                     2, 2,
                     3, 3, 3, 3, 3, 3, 3,
                     4, 4, 4, 4,
                     5, 5, 5,
                  )\
               )
         elif (self.person.state == 3):
            self.person.position = random.choice(\
               (\
                  0, 0, 0,
                  1,
                  2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                  3, 3, 3, 3, 3, 3, 3,
                  4, 4, 4,
                  5, 5,
               )\
            )
      
      return 0
   
   def change_location (self):
      old_loc = self.person.location
      if (self.person.location == 0):
         self.person.position = random.choice(\
            (\
               0, 0, 0,
               1, 1, 1, 1, 1,
            )\
         )
      else:
         pnegative_loc = self.person.location - 2
         if (self.person.location < 3):
            pnegative_loc = 0
         ppositive_loc = self.person.location + 3
         if ((self.person.location + 3) >= (self.house.availableroomid - 1)):
            ppositive_loc = self.house.availableroomid - 1
         if ((self.person.state > 1) and (self.person.position > 1)):
            self.person.location = random.randint(pnegative_loc, ppositive_loc)
      
      # Turn on all appliances in current location.
      if ((self.person.location != old_loc) and \
         (self.person.location != 0)):
         for appliance in self.house.rooms[self.person.location].appliances:
            if (type(appliance).__name__ == "Fan"):
               appliance.signal("power", True)
               appliance.signal(\
                  "speed", \
                  random.randint(\
                     int(appliance.maxspeed/2), \
                     appliance.maxspeed, \
                  ), \
               )
            elif (type(appliance).__name__ == "Light"):
               appliance.signal("power", True)
               appliance.signal(\
                  "brightness", \
                  random.randint(\
                     int(appliance.maxbrightness/2), \
                     appliance.maxbrightness, \
                  ), \
               )
            elif (type(appliance).__name__ == "TV"):
               appliance.signal("power", True)
               appliance.signal(\
                  "volume", \
                  random.randint(\
                     int(appliance.maxvolume/2), \
                     appliance.maxvolume, \
                  ), \
               )
               appliance.signal(\
                  "channel", \
                  random.randint(\
                     0, \
                     appliance.maxchannel, \
                  ), \
               )
               appliance.signal(\
                  "brightness", \
                  random.randint(\
                     int(appliance.maxbrightness/2), \
                     appliance.maxbrightness, \
                  ), \
               )
      
      return 0
# Guard line - 79th character at end (length = 79):
# -----------------------------------------------------------------------------
