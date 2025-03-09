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

RAD_TO_DEG = 180/3.14159265358979323846
DEG_TO_RAD = 3.14159265358979323846/180

def getpos():
    """
    Parse la trame de position envoyee par l'embase a la raspi.
    La trame est de la forme: "x y r\n"
    """
    parse_error_flag = 1

    while(parse_error_flag):
        try:
            # Tant que la trame n'est pas correctement parsee, on continue de lire
            port_embase.reset_input_buffer()  # Flush the input buffer
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
while(getpos()[0] != 0): print(getpos())

port_embase.write(AVANCER)
while(getpos()[0] < 0.5) : print(getpos())

port_embase.write(STOP)
sleep(0.5)

port_embase.write(TRANSLATION_DROITE)
while(getpos()[1] < 0.2) : print(getpos())

port_embase.write(STOP)
sleep(0.5)

port_embase.write(RECULER)
while(getpos()[0] > 0) : print(getpos())

port_embase.write(STOP)
sleep(0.5)

port_embase.write(TRANSLATION_GAUCHE)
while(getpos()[1] > 0) : print(getpos())

port_embase.write(STOP)