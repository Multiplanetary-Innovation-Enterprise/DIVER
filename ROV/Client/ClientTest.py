from SocketWriter import SocketWriter
from SocketReader import SocketReader
from ServerConnection import ServerConnection
from ROVMessaging.Publisher import *
from ROVMessaging.Message import *
from ROVMessaging.MessageChannel import *
from ROVMessaging.MessageType import *
from SubWriter import SubWriter
from PubListener import PubListener
import time
import sys

port = 25000
host = sys.argv[1]

s = ServerConnection(host, port)
w = SocketWriter(s)
sub = SubWriter(w)
mc = MessageChannel()
pub = PubListener(None, mc)
bool = mc.subscribe(MessageType.ACTION, sub)
# message = Message(MessageType.ACTION, "Shutdown")
# pub.sendMessage(message, mc)
# s.close()

#start keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread

while True:
    x = 0


def on_press(key):
    # if key == keyboard.Key.esc:
    #     return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'w', 's', 'space', 'esc']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        message = Message(MessageType.ACTION, "this is an action message")
        pub.sendMessage(message, mc)
