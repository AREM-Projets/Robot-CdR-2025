#commandes embase
EQUIPE_BLEUE = b'b'
EQUIPE_JAUNE = b'j'
PROG_3_PANNEAUX = b'3'
PROG_6_PANNEAUX = b'6'
INIT = b'i' #restart sans redemarrer la carte
START = b's'
WAIT = b'w'
OK = b'k'
#messages de l'embase
POS_PANNEAU_OK = b'p'





import serial
import time
port_embase = serial.Serial('/dev/embase', 115200) #timeout en secondes

time.sleep(1)

port_embase.write(EQUIPE_BLEUE)
port_embase.write(PROG_3_PANNEAUX)
port_embase.write(INIT)

time.sleep(1)

port_embase.write(START)
