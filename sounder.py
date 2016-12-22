from psonic import  *
import RPi.GPIO as GPIO
import time

button1_pin = 35
button2_pin = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(True):
  if GPIO.input(button1_pin):
    print("high")
    #use_synth(SAW)
  else:
    print("low")
    #use_synth(ZAWA)
  if GPIO.input(button2_pin):
    play(90)
    #sleep(0.5)
  #else:
  #  play(70)
  #  sleep(0.1)
  time.sleep(0.5)
  #play(72)
  #sleep(0.5)
  #play(79)
  #sleep(0.5)
  #use_synth(DTRI)
  #play(72)
  #sleep(0.5)
  #play(79)
  #sleep(2)
