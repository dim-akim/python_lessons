import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - работа с сетью, SOCK_STREAM - протокол TCP
server_address = ('0.0.0.0', 2222)
s.bind(server_address)
s.listen(10)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data == 'close':
            break
        conn.send(data)
    conn.close()
