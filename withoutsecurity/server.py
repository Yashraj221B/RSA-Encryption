import socket
import cryptography.fernet
import threading

server_addr = ("localhost",0x221A)
client_addr = ("localhost",0x221B)
intercept_addr = ("localhost",0x221C)

# Shitty code


def comm_thread(client):
    while True:
        data = input("Enter Message: ").encode("utf-8")
        client.send(data)


def recv_thread(client):
    while True:
        data = client.recv(2048)
        print("Client:", data.decode("utf-8"))


if __name__ == "__main__":
    server = socket.socket()
    server.bind(server_addr)
    server.listen(10)

    client, addr = server.accept()

    thread1 = threading.Thread(target=comm_thread,args=(client,))
    thread2 = threading.Thread(target=recv_thread,args=(client,))
    thread1.start()
    thread2.start()
