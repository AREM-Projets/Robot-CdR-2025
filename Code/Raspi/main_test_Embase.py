from Embase import *

embase = Embase()
embase.connect()
embase.reset()
embase.move(AVANCER)
while(embase.getpos()[0] < 0.1) : print(embase.getpos())
embase.stop()