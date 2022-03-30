import cv2 as cv


camera = cv.VideoCapture(0)
camera.set(cv.CAP_PROP_FRAME_WIDTH, 2560)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, 1440)

while True:
    ret, frame = camera.read()

    cv.imshow("Frame", frame)

    if cv.waitKey(1) == ord('q'):
        break
