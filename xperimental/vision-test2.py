from picamera import PiCamera

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1920, 1080))
# allow the camera to warmup
time.sleep(0.1)

# initialize the frame and the variable used to indicate
# if the thread should be stopped


def update():

	numFrames = 1
	newFrameTime = 1
	prevFrameTime = 0

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		print("Frame!!!!!")
		# grab the raw NumPy array representing the image, then initialize the timestamp
		# and occupied/unoccupied text
		image = frame.array
		# show the frame
		cv2.imshow("Frame", image)
		key = cv2.waitKey(1) & 0xFF
		# clear the stream in preparation for the next frame
		rawCapture.truncate(0)
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			break
		print("SEC: "  + str(newFrameTime - prevFrameTime))
		fps = int(1 / (newFrameTime - prevFrameTime))
		prevFrameTime = newFrameTime

		print("FPS: " + str(fps))

		newFrameTime = time.time()

threading.Thread(target=update, args=()).start()
