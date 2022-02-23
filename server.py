from socket import *

def run_server():
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



if __name__ == "__main__":
    print('run...')
    run_server()




