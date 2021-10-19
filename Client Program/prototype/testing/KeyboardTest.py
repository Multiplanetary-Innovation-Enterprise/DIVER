import keyboard
import queue

wasReleased = 1
queueRunning = 0

q = queue.Queue(maxsize=1000)

speedReleased = 1

speed = 0

def pressed(e):
    global wasReleased
    global queueRunning

    if wasReleased == 1:
        q.put("Forward @ " + str(speed))
       # print("W Pressed " + str(q.qsize()) + "\n");
        wasReleased = 0


        if not queueRunning:
            processQueue(q)

def realease(e):
    global wasReleased

    if wasReleased == 0:
        q.put("Stop Forward")
        #print("W released " + str(q.qsize()) + "\n");
        wasReleased = 1

        if not queueRunning:
            processQueue(q)


def increaseSpeed(e):
    global speedReleased
    global speed

    q.put("Increase Speed")
    speedReleased = 0
    speed += 0.1


    if not queueRunning:
        processQueue(q)

def stopIncreaseSpeed(e):
    global speedReleased
    global queueRunning

    q.put("Stop Increasing Speed")
    speedReleased = 1

    if not queueRunning:
        processQueue(q)


keyboard.on_press_key('w', pressed, True)

keyboard.on_release_key('w', realease)

keyboard.on_press_key('up', increaseSpeed, True)
keyboard.on_release_key('up', stopIncreaseSpeed)


def processQueue(q):
    global queueRunning

    queueRunning = 1

    while not q.empty():
        print(q.get() + " " + str(q.qsize()) + "\n");

    queueRunning = 0
