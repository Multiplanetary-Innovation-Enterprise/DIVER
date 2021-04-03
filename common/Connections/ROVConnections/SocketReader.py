from ROVConnections.SocketConnection import SocketConnection
from ROVConnections.ClientConnection import ClientConnection
from ROVConnections.ServerConnection import ServerConnection
from ROVConnections.Reader import Reader
from ROVMessaging.Message import Message
from ROVMessaging.MessageType import MessageType
import pickle
import time

class SocketReader(Reader):
    __socket = None
    MAX_MSG = 8192

    def __init__(self, socket):
        self.__socket = socket

    def getSocket(self):
        return self.__socket

    def decode(self, message):
        return pickle.loads(message)

    def receive(self):
        msg = self.__recv_timeout(self.__socket, 0.5)
        if (msg != None):
            return self.decode(msg)
        return msg

    def __recv_timeout(self, the_socket, timeout): #NOTE: may need to modify so it blocks for the first chunk
        #make socket non blocking
        the_socket.setblocking(0)

        #total data partwise in an array
        total_data=[];
        data='';

        #beginning time
        begin=time.time()
        while 1:
            #if you got some data, then break after timeout
            if total_data and time.time()-begin > timeout:
                break

            #if you got no data at all, wait a little longer, twice the timeout
            elif time.time()-begin > timeout*2:
                break

            #recv something
            try:
                data = the_socket.recv(self.MAX_MSG)
                if data:
                    total_data.append(data)
                    #change the beginning time for measurement
                    begin = time.time()
                else:
                    #sleep for sometime to indicate a gap
                    time.sleep(0.1)
            except:
                pass

        if (len(total_data) > 0):
            #join all parts to make final string
            return b''.join(total_data)
        else:
            return None #NOTE: still errors, needs to be a byte-like object
