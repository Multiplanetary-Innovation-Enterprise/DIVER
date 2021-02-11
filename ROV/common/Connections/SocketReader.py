from SocketConnection import SocketConnection
from ClientConnection import ClientConnection
from ServerConnection import ServerConnection
from Message import Message
import pickle
import time

class SocketReader(Reader):
    __socket = None
    MAX_MSG = 8192

    def __init__(self, socket):
        self.__socket = socket.get()

    def decode(self, message):
        return pickle.loads(message)

    def receive(self):
        return self.decode(__recv_timeout(self.__socket, 2))

    def __recv_timeout(the_socket,timeout):
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

        #join all parts to make final string
        return ''.join(total_data)
