import time
import picamera
import numpy as np
from PIL import Image

RECORD_TIME = 5  # number of seconds to record

WRITE_IMAGES = False

# SENSOR_MODE = 4  # 1640x1232, full FoV, binning 2x2
# RESOLUTION = (1640, 1232)
# RESOLUTION = (820, 616)

# SENSOR_MODE = 6  # 1280x720, partial FoV, binning 2x2
# RESOLUTION = (1280, 720)

SENSOR_MODE = 7  # 640x480, partial FoV, binning 2x2
RESOLUTION = (640, 480)

# FRAME_RATE = 90
FRAME_RATE = 120
# FRAME_RATE = 200

FPS_MODE_OFF = 0
FPS_MODE_T0 = 1
FPS_MODE_FBF = 2
FPS_MODE = FPS_MODE_OFF

# Calculate the actual image size in the stream (accounting for rounding
# of the resolution)
# Capturing yuv will round horizontal resolution to 16 multiple and vertical to 32 multiple
# see: https://picamera.readthedocs.io/en/release-1.12/recipes2.html#unencoded-image-capture-yuv-format
fwidth = (RESOLUTION[0] + 31) // 32 * 32
fheight = (RESOLUTION[1] + 15) // 16 * 16
print(f'frame size {fwidth}x{fheight}')

frame_cnt = 0
t0 = None
t_prev = None


def write_luminance_disk(y_data, frame):
    filename = f'frame-{frame}.bmp'
    im = Image.fromarray(y_data, mode='L')  # using luminance mode
    im.save(filename)


class RecordingOutput(object):
    """
    Object mimicking file-like object so start_recording will write each frame to it.
    See: https://picamera.readthedocs.io/en/release-1.12/api_camera.html#picamera.PiCamera.start_recording
    """

    def write(self, buf):
        global frame_cnt, t_prev
        # write will be called once for each frame of output. buf is a bytes
        # object containing the frame data in YUV420 format; we can construct a
        # numpy array on top of the Y plane of this data quite easily:
        y_data = np.frombuffer(buf, dtype=np.uint8, count=fwidth * fheight).reshape((fheight, fwidth))

        # actual processing
        if WRITE_IMAGES and frame_cnt % 20 == 0:
            write_luminance_disk(y_data, frame_cnt)

        frame_cnt += 1

        if FPS_MODE is not FPS_MODE_OFF:
            if FPS_MODE == FPS_MODE_FBF:
                # frame by frame difference
                dt = time.time() - t_prev  # dt
                t_prev = time.time()
                fps = 1.0 / dt
            else:
                # calculation based on time elapsed since capture start
                dt = time.time() - t0  # dt
                fps = frame_cnt / dt

            if frame_cnt % 10 == 0:
                print(f'fps: {round(fps, 2)}')

    def flush(self):
        pass  # called at end of recording


with picamera.PiCamera(
        sensor_mode=SENSOR_MODE,
        resolution=RESOLUTION,
        framerate=FRAME_RATE
) as camera:
    print('camera setup')
    camera.rotation = 180

    time.sleep(2)  # let the camera warm up and set gain/white balance

    print('starting recording')
    output = RecordingOutput()

    t0 = time.time()  # seconds
    t_prev = t0

    camera.start_recording(output, 'yuv')
    camera.wait_recording(RECORD_TIME)
    camera.stop_recording()

    dt = time.time() - t_prev
    print(f'total frames: {frame_cnt}')
    print(f'time recording: {round(dt, 2)}s')
    fps = frame_cnt / dt
    print(f'fps: {round(fps, 2)}s')

print('done')
