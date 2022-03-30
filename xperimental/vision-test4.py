from io import BytesIO
from time import sleep
from picamera import PiCamera

# Create an in-memory stream
my_stream = BytesIO()
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 60

camera.start_preview()
# Camera warm-up time
sleep(10)
camera.capture(my_stream, 'jpeg')
