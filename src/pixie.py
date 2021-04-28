import signal

from Pixie.main import Main

main = Main()
signal.signal(signal.SIGINT, main.stop)
main.run()
