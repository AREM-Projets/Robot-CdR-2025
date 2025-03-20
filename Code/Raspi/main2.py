from Embase import *

embase = Embase()
embase.odo_reset()
embase.move(AVANCER)
while(embase.getpos()[0] < 0.2) : print(embase.getpos())
embase.stop()