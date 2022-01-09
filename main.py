import logging
import socket


def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(("0.0.0.0", 8000))
    server_sock.listen()

    while True:
        (client_sock, address) = server_sock.accept()

        request = client_sock.recv(1024).decode()
        logging.info(request)

        with open("./templates/hello_world.html", "r") as template:
            response = template.read()

        client_sock.sendall(response.encode())
        client_sock.close()


if __name__ == "__main__":
    main()
