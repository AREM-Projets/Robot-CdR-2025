import serial
from time import sleep

AVANCER                 = b'8'
RECULER                 = b'2'
TRANSLATION_GAUCHE      = b'4'
TRANSLATION_DROITE      = b'6'
ROTATION_GAUCHE         = b'7'
ROTATION_DROITE         = b'9'
STOP                    = b'5'
RESET_POS               = b'.'

def getpos():
    parse_error_flag = 1

    while(parse_error_flag):
        try:
            port_embase.read()
            sleep(0.1)
            x = float(port_embase.readline().decode().split()[0].replace('\x00', ''))
            y = float(port_embase.readline().decode().split()[1].replace('\x00', ''))
            r = float(port_embase.readline().decode().split()[2].replace('\x00', ''))
            

            parse_error_flag = 0
        except:
            pass

    return  (x, y, r)


#connexion a l'embase
try:
    print("[ ... ] Connexion embase")
    port_embase = serial.Serial('/dev/embase', 115200, timeout=1) #timeout en secondes
    print("[ OK  ] Connexion embase")
except:
    print("[ NOK ] Connexion embase: echec")





"""
Sequence de deplacement

Format de la trame de position envoyee par l'embase: "%.4f %.4f %.4f\n"
"""

port_embase.write(RESET_POS)
while(getpos()[0] != 0): pass

port_embase.write(AVANCER)
while(getpos()[0] < 0.5) : pass

port_embase.write(STOP)

port_embase.write(RECULER)
while(getpos()[0] > 0) : pass

port_embase.write(STOP)
