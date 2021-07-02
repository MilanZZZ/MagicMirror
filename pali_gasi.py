from gpiozero import Button
from signal import pause 
from time import sleep
import subprocess

print("this is the one in the home dir")

radar = Button(17, pull_up=False) 

def turn_off(): 
	print(subprocess.run(["/opt/vc/bin/tvservice -o"], 
                     shell=True))
	radar.wait_for_press()
def turn_on():
    print(subprocess.run(["/opt/vc/bin/tvservice --preferred && sudo chvt 6 && sudo chvt 7",], 
                     shell=True))
    sleep(40)
radar.wait_for_press()

while True:
    if(radar.is_pressed):
        turn_on()
    else:
        turn_off()


 