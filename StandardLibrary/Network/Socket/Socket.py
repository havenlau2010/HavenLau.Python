import socket

def create_socket_server():
    # Address
    HOST = '192.168.0.106'
    PORT = 8000
    reply = 'Yes'

    #Configure socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))

    # passively wait, 3: maximum number of connections in the queue
    s.listen(3)

    # accept and establish connection
    conn,addr = s.accept()

    # receive message
    request = conn.recv(1024)

    print('request is: ',request)
    print('Connected by', addr)

    # send message
    conn.sendall(reply)

    # close connection
    conn.close()

def create_socket_client():
    # Address
    HOST = '192.168.0.106'
    PORT = 8000

    request = 'can you hear me?'

    # configure socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # send message
    s.sendall(request)
    # receive message
    reply = s.recv(1024)
    print('reply is: ',reply)
    # close connection
    s.close()