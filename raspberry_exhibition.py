#Exhibition Demo

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from ultrasonic import sonic
from claw import Arm
from ioc import IOController
from time import sleep
import webinterface

if __name__ == "__main__":
    IOController.begin()
    claw = Arm()
    webinterface.setClawObj(claw)
    webinterface.begin()
    
    while True:
        distance=sonic()
        
        if distance >= 10 and distance <= 15:
            print("Arm move")
            sleep(1)
        
        sleep(0.2)
