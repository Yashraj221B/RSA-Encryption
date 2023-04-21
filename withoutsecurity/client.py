import socket
import cryptography
import threading

server_addr = ("localhost",0x221A)
client_addr = ("localhost",0x221B)
intercept_addr = ("localhost",0x221C)

# Shitty code


def comm_thread(server):
    while True:
        data = input("Enter Message: ").encode("utf-8")
        server.send(data)


def recv_thread(server):
    while True:
        data = server.recv(2048)
        print("Client:", data.decode("utf-8"))


if __name__ == "__main__":
    client = socket.socket()
    client.bind(client_addr)
    client.connect(intercept_addr)
    thread1 = threading.Thread(target=comm_thread,args=(client,))
    thread2 = threading.Thread(target=recv_thread,args=(client,))
    thread1.start()
    thread2.start()
