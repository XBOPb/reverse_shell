import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8888))                               # using all available ips
s.listen(5)                                             # up to 5 clients
client, addr = s.accept()
while True:
    command = str(input('Command: '))
    client.send(command.encode())
    if command.lower() == 'exit':
        break
    result = client.recv(1024).decode()
    print(result)
client.close()
s.close()
