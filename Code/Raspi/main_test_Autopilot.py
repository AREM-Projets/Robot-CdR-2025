from Autopilot import *


auto = Autopilot("Code/Raspi/trajectoire.txt")
auto.move(0.2, 0.2, 0)
auto.home()