from socket import *


def run_tcp_server():
    server_port = 8080
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Ready to receive")

    connection, addr = server_socket.accept()
    while True:
        msg = connection.recv(2048).decode()
        if msg == "":
            connection.close()
            print("Connection closed")
            break
        modif_msg = 'Message is "' + msg + '"'
        connection.send(modif_msg.encode())


def run_udp_server():
    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024

    msgFromServer = "Hello UDP Client"
    bytesToSend = str.encode(msgFromServer)

    # Create a datagram socket
    UDPServerSocket = socket(family=AF_INET, type=SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    # Listen for incoming datagrams

    while (True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = f"Message from Client:{message}"
        clientIP = f"Client IP Address:{address}"

        print(clientMsg)
        print(clientIP)

        # Sending a reply to client
        UDPServerSocket.sendto(bytesToSend, address)


if __name__ == "__main__":
    print('run...')
    # run_tcp_server()
    run_udp_server()