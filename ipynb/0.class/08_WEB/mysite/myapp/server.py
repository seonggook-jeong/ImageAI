import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 80))
server_socket.listen(0)
print('listening')

client_socket, addr = server_socket.accept()
print('accepting')

data = client_socket.recv(65535)
print(data.decode())