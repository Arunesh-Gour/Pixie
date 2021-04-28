import time

class AutoExecutor:
   def __init__ (self):
      self.killthread = False
   
   def auto_execute (self, exec_function, times=None, interval=60, timespeed=60):
      marktime = 0
      hittime = 0
      while (self.killthread == False):
         time.sleep(1)
         marktime += (1 * timespeed)
         if (marktime >= interval):
            hittime += 1
            marktime = 0
            exec_function()
            if ((times != None) and (times > 0)):
               if (hittime >= times):
                  self.killthread = True
      
      self.killthread = False
      return 0
   
   def kill (self):
      self.killthread = True
