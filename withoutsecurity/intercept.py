import socket
import threading

server_addr = ("localhost",0x221A)
client_addr = ("localhost",0x221B)
intercept_addr = ("localhost",0x221C)


#Very simple shitty code
#STATS:
# RUBT: 35%
# DOC: 10%
# SMCT: 60%

def server_thread(server:socket.socket,client:socket.socket):
    while True:
        recv = server.recv(2048)
        print("Server:",recv.decode("utf-8"))
        client.send(recv)

def client_thread(server:socket.socket,client:socket.socket):
    while True:
        recv = client.recv(2048)
        print("Client:",recv.decode("utf-8"))
        server.send(recv)

if __name__ == "__main__":
    manager = socket.socket(socket.AF_INET)
    manager.bind(intercept_addr)
    manager.listen(10)

    server = socket.socket()
    server.connect(server_addr)

    client,addr = manager.accept()

    thread1 = threading.Thread(target=server_thread,args=(server,client))
    thread2 = threading.Thread(target=client_thread,args=(server,client))
    thread1.start()
    thread2.start()
