import paramiko
import socket
from scp import SCPClient
from ClientApp import *

#create paramiko SSHClient and connect to Pi
print("SSHing into ROV...")
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(socket.gethostbyname("raspberrypi"),port=22,username="pi",password="Mine21",)

#use SCP to transfer DIVER folder to Pi
scpClient = SCPClient(sshClient.get_transport())
scpClient.put('../../../../DIVER', recursive=True, remote_path='/home/pi/DIVER')

#execute ROV Launcher (without hanging or quitting when the SSH logs out) and then quit 
sshClient.exec_command('nohup "python3 /home/pi/DIVER/ROV Program/src/ROVLauncher.py" & exit')
print("Successfully started ROV Launcher on ROV")

sshClient.close()

print("Starting Client Launcher...")
#Python equivalent of main function
def main():
    #Starts the ROV client program
    rovClient = ClientApp()
    rovClient.start()

#Checks that the code is being executed and not imported
if __name__ == "__main__":
    main()