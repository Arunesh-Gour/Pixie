import signal
import multiprocessing

from .core import Automator

automator = Automator.Automator()
automatorprocess = multiprocessing.Process(\
   target=automator.automate, \
)

def stop ():
   global automator, automatorprocess
   
   automator.kill()
   time.sleep(5)
   automatorprocess.kill()
   del automatorprocess, automator
   time.sleep(5)
   exit(0)

signal.signal(signal.SIGINT, stop)
signal.signal(signal.SIGTERM, stop)

automatorprocess.start()
automatorprocess.join()
