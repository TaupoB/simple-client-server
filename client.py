from socket import *

def run_tcp_client():
    server_name = 'localhost'
    server_port = 8080
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    while True:
        msg = input("input: ")
        if msg == '':
            client_socket.close()
            break
        client_socket.send(msg.encode())
        modif_msg = client_socket.recv(2048)
        print('From server: ', modif_msg.decode())


def run_udp_client():

    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

    # Send to server using created UDP socket
    while True:
        msgFromClient = input()
        if msgFromClient == '':
            break
        bytesToSend = str.encode(msgFromClient)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = f"Message from Server {msgFromServer[0]}"
        print(msg)

if __name__ == "__main__":
    # run_tcp_client()
    run_udp_client()



