from MessageChannel import MessageChannel
from Message import Message
from MessageType import MessageType
from Subscriber import Subscriber

import time
import concurrent.futures
import threading
from multiprocessing import Process

class TestSubscriber(Subscriber):
    def recieveMessage(self, message:Message):
        num = 10

        print("----------------------------------------------1 start: " + str(message.getType()) + "------------------------------------------------")
        print("Thread id: " + str(threading.get_ident()))
        t1 = time.time()
        # for i in range(0, 500000):
        #     num = num + num ^ num

            # print("---------------1------------")

        t2 = time.time()

        print("Elapsed 1: " + str(t2-t1))
        print("----------------------------------------------1 done: " + str(message.getType()) + "------------------------------------------------")

class TestSubscriber2(Subscriber):

    def recieveMessage(self, message:Message):
        print("----------------------------------------------2 start: " + str(message.getType()) + "------------------------------------------------")
        print("Thread id: " + str(threading.get_ident()))
        num = 10
        # for i in range(0, 1000):
        #     num = num * 10
            # print("---------------2------------")

        print("--------------------------------------------2 done: " + str(message.getType()) + "------------------------------------------------")


def run1():
    message = Message(MessageType.ACTION, "Move!")
    message2 = Message(MessageType.SYSTEM_STATUS, "Do")
    print("Messssssssssss1")
    messageChannel.broadcast(message)

    time.sleep(3)
    print("Messssssssssss1.2")
    messageChannel.broadcast(message)
    time.sleep(3)

def run2():
    message = Message(MessageType.ACTION, "Move!")
    message2 = Message(MessageType.SYSTEM_STATUS, "Do")
    print("Messssssssssss2")
    print("Threads: " + str(threading.active_count()))
    messageChannel.broadcast(message2)

    time.sleep(1)
    print("Messssssssssss2.2")
    messageChannel.broadcast(message2)


if __name__ == '__main__':
    messageChannel = MessageChannel()
    messageChannel.setProcessInParallel(True)
    message = Message(MessageType.ACTION, "Move!")
    message2 = Message(MessageType.SYSTEM_STATUS, "Do")

    subscriber = TestSubscriber()
    # subscriber2 = TestSubscriber()
    subscriber3 = TestSubscriber2()

    messageChannel.subscribe(MessageType.ACTION, subscriber)
    # messageChannel.subscribe(MessageType.SYSTEM_STATUS, subscriber)
    # messageChannel.subscribe(MessageType.ACTION, subscriber2)
    messageChannel.subscribe(MessageType.ACTION, subscriber3)
    messageChannel.subscribe(MessageType.SYSTEM_STATUS, subscriber3)

    message = Message(MessageType.ACTION, "Move!")

    startTime = time.time()

    # thread1 = threading.Thread(target=run1)
    # thread2= threading.Thread(target=run2)
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()

    # process1 = Process(target=run1, args=(messageChannel,))
    # process2 = Process(target=run2, args=(messageChannel,))
    #
    # process1.start()
    # process2.start()

    messageChannel.broadcast(message)
    messageChannel.broadcast(message)
    messageChannel.broadcast(message2)
    messageChannel.broadcast(message2)

    # process1.join()
    # process2.join()
    endTime = time.time()
    print("Elapsed: " + str((endTime - startTime)) + " s")
    # print("Elapsed: " + str(1000.0 * (endTime - startTime)) + " ms")
