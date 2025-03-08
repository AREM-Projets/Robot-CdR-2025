import serial
import threading

# Configuration du port série
port = serial.Serial('/dev/embase', 115200)

def read_from_port():
    """Lire en permanence les données reçues sur le port série."""
    try:
        buffer = ""
        while True:
            if port.in_waiting > 0:
                buffer += port.read(port.in_waiting).decode('utf-8')
                if "\n" in buffer:
                    lines = buffer.split("\n")
                    for line in lines[:-1]:
                        print(f"Reçu : {line}")
                    buffer = lines[-1]  # Conserver les données partielles
    except Exception as e:
        print(f"Erreur lors de la lecture du port série : {e}")

def write_to_port():
    """Envoyer des commandes sur le port série."""
    try:
        while True:
            cmd = input("$: ")
            port.write(cmd.encode())
    except Exception as e:
        print(f"Erreur lors de l'envoi de données : {e}")

# Démarrer un thread pour lire en permanence le port série
read_thread = threading.Thread(target=read_from_port, daemon=True)
read_thread.start()

# Boucle principale pour écrire sur le port série
write_to_port()
