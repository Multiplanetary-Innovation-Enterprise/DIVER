import paramiko
import socket
print("SSHing into ROV...")
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(socket.gethostbyname("raspberrypi"),port=22,username="pi",password="Mine21",)
print("Successfully started python on ROV")
try:
    stdin,stdout,stderr = sshClient.exec_command('cd Programs/ROV/src ; python3 ROVLauncher.py')
except KeyboardInterrupt:
    sshClient.exec_command('sudo shutdown -h now')
    sshClient.close()
