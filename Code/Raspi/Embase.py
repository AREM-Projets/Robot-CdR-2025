"""
Classe d'interface avec l'embase du robot cdr"
"""
import serial
from time import sleep
import datetime as dt


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




class Embase:
    def __init__(self, port="/dev/embase", baudrate=115200):
        self.log = open("Code/Raspi/log.txt", 'a')
        self.port = None
        self.port_name = port
        self.port_baudrate = baudrate

        
    def connect(self):
        """
        Connecte l'embase a la raspi
        """
        try:
            print("[ ... ] Connexion embase")
            self.log.write("\n" + str(dt.datetime.now()) + " - Connexion embase ...")
            self.port = serial.Serial(self.port_name, self.port_baudrate, timeout=1) #timeout en secondes
            print("[ OK  ] Connexion embase")
            self.log.write("\n" + str(dt.datetime.now()) + " - Connexion embase OK")
        
        except:
            print("[ NOK ] Connexion embase: echec")
            self.log.write("\n" + str(dt.datetime.now()) + " - Connexion embase NOK")

            
    def getpos(self):
        """
        Parse la trame de position envoyee par l'embase a la raspi.
        La trame est de la forme: "x y r\n"
        """
        parse_error_flag = 1

        while(parse_error_flag):
            try:
                # Tant que la trame n'est pas correctement parsee, on continue de lire
                self.port.reset_input_buffer()  # Flush the input buffer
                x = float(self.port.readline().decode().split()[0].replace('\x00', ''))
                y = float(self.port.readline().decode().split()[1].replace('\x00', ''))
                r = float(self.port.readline().decode().split()[2].replace('\x00', ''))
                
                self.log.write("\n" + str(dt.datetime.now()) + f" - Position: {x}, {y}, {r}")
                print(f"Position: {x}, {y}, {r}")

                parse_error_flag = 0
            except:
                pass

        return  (x, y, r)
    
    def move(self, d):
        self.port.write(d)

    def stop(self):
        self.port.write(STOP)

    def reset(self):
        self.port.write(RESET_POS)
        while(self.getpos()[0] != 0): pass #print(self.getpos())