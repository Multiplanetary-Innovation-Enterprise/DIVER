from components.sensors.cameras.PiCamera import PiCamera

camera = PiCamera()
camera.setResolution(640, 480)

image = camera.getFrame()

print(image)

image.save('test2.jpg')
