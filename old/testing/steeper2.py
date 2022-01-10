from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

while True:
  print("1")
  GPIO.output(5, GPIO.HIGH);
  GPIO.output(6, GPIO.HIGH);
  GPIO.output(13, GPIO.LOW);
  GPIO.output(19, GPIO.LOW);

  sleep(0.02)
  print("2")
  GPIO.output(5, GPIO.LOW);
  GPIO.output(6, GPIO.HIGH);
  GPIO.output(13, GPIO.HIGH);
  GPIO.output(19, GPIO.LOW);

  sleep(0.02)
  print("3")
  GPIO.output(5, GPIO.LOW1);
  GPIO.output(6, GPIO.LOW);
  GPIO.output(13, GPIO.HIGH);
  GPIO.output(19, GPIO.HIGH);

  sleep(0.02)
  print("4")
  GPIO.output(5, GPIO.HIGH);
  GPIO.output(6, GPIO.LOW);
  GPIO.output(13, GPIO.LOW);
  GPIO.output(19, GPIO.HIGH);

  sleep(0.02)

GPIO.cleanup()
