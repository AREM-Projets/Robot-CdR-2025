# Robot-CdR-2025

Repo contenant l'ensemble du code du robot de la coupe de France de Robotique 2025.

## TODO

- Faire un script bash qui démarre le main.py du robot, crées la fifo_lidar_to_raspi et démarre le driver_lidar

## LIDAR

>**Compilation du driver lidar**: ``bash driver_lidar_compilation.sh``
>**Démarrage du driver lidar**: ``./driver_lidar --channel --serial /dev/ttyUSB0 460800``