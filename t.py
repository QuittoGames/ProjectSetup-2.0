from datetime import time
from os import system
from time import sleep

lcoal_time = time.hour

while True:
    if lcoal_time == 0:
        system("sudo shutdown now")
    sleep(1)