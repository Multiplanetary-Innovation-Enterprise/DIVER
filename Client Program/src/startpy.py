import paramiko
import socket
print("SSHing into ROV...")
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshClient.connect(socket.gethostbyname("raspberrypi"),port=22,username="pi",password="Mine21",)
stdin,stdout,stderr = sshClient.exec_command('cd Programs/ROV/src ; python3 ROVLauncher.py ')
for line in stdout.read().splitlines():
    print(line.decode())
for line in stderr.read().splitlines():
    print(line)
self.sshClient.close()
print("Successfully started python on ROV")
