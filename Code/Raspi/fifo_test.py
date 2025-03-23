import os
from time import sleep


lidar = open("/home/cdr/Robot-CdR-2025/Code/Raspi/fifo_lidar_to_raspi", 'r')


while(1):
    # print(lidar.readline())
    raw_output = lidar.readline().replace('\x00', '').split()
    numeric_output = [float(val) for val in raw_output]
    print(numeric_output)
