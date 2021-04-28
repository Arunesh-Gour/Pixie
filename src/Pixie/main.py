import signal
import multiprocessing
import time

from .core import Automator

class Main:
   def __init__ (self):
      #self.lock = multiprocessing.Lock()
      #self.called_times = 0
      self.automator = Automator.Automator()
      self.automatorprocess = multiprocessing.Process(\
         target=self.automator.automate, \
      )
      
      # signal.signal(signal.SIGINT, self.stop)
      # signal.signal(signal.SIGTERM, self.stop)
      
   def run (self):
      self.automatorprocess.start()
      self.automatorprocess.join()
   
   def stop (self, signalnumber, currentstackframe):
      self.automator.kill()
      print("--EXITING--\n" \
         + "Stopped by signal {0}\n".format(signalnumber)\
      )
   
   """
   def stop (self, signalnumber, currentstackframe):
      self.lock.acquire()
      if (self.called_times == 0):
         self.called_times += 1
         self.automator.kill()
         time.sleep(5)
         print("--EXITING--")
         del self.automator
         time.sleep(5)
         print("Stopped by signal {0}".format(signalnumber))
      self.lock.release()
      exit(0)
   """
