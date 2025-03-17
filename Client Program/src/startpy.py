import paramiko
import socket
from ClientApp import *

print("SSHing into ROV...")
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(socket.gethostbyname("raspberrypi"),port=22,username="pi",password="Mine21",)
stdin,stdout,stderr = sshClient.exec_command('cd Programs/ROV/src && nohup "python3 ROVLauncher.py" & exit')
for line in stdout.read().splitlines():
    print(line.decode())
for line in stderr.read().splitlines():
    print(line)
print("Successfully started python on ROV")



#Python equivalent of main function
def main():
    #Starts the ROV client program
    rovClient = ClientApp()
    rovClient.start()

#Checks that the code is being executed and not imported
if __name__ == "__main__":
    main()