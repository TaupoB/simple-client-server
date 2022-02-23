from socket import *

def run_client():
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


if __name__ == "__main__":
    run_client()



