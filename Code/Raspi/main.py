import serial

AVANCER                 = b'8'
RECULER                 = b'2'
TRANSLATION_GAUCHE      = b'4'
TRANSLATION_DROITE      = b'6'
ROTATION_GAUCHE         = b'7'
ROTATION_DROITE         = b'9'
STOP                    = b'5'
RESET_POS               = b'.'

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
print("RESET_POS")
port_embase.write(RESET_POS)
print("AVANCER")
port_embase.write(AVANCER)

# on attends d'avoir fait 0.1m selon le devant du robot au demarrage et on s'arrete
print("Attente d'avoir atteint x=0.1m")
while(float(port_embase.readline().split()[0]) < 0.1) : pass
print("Position atteinte")

print("STOP")
port_embase.write(STOP)