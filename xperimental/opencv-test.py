import cv2 as cv
import time

camera = cv.VideoCapture(0)
camera.set(cv.CAP_PROP_FRAME_WIDTH, 2560)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, 1440)

currTime = 0
lastTime = 0

while True:
    ret, frame = camera.read()

    cv.imshow("Frame", frame)

    if cv.waitKey(1) == ord('q'):
        break

    lastTime = currTime
    currTime = time.time_ns()

    print("Elapsed: " + str((currTime - lastTime) / 1000000000))
