import socket
import _thread
import ssl
import select

listen_host = "0.0.0.0"
listen_port = 5000

target_host = "104.18.101.57"
target_port = 443

def exchange_loop(client, remote):
    while True:
        data = client.recv(2048 * 2)
        if data:
            if b"progress.liara.run" in data:
                data = data.replace(b"progress.liara.run", b"shadowcoder.shayangosi1383.workers.dev")
            remote.sendall(data)
        else:
            client.shutdown(socket.SHUT_RD)
            remote.shutdown(socket.SHUT_WR)
            break

def run():
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind((listen_host, listen_port))
        dock_socket.listen()

        print("*** listening on %s:%i ***" % ( listen_host, listen_port ))

        while True:
            client_socket, client_address = dock_socket.accept()
            print("*** from %s:%i to %s:%i ***" % ( client_address, listen_port, target_host, target_port ))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_host, target_port))
            context = ssl.create_default_context()
            server_socket = context.wrap_socket(s, server_hostname="d342d11e-d424-4583-b36e-524ab1f0afa4.shayangosi1383.workers.dev")
            _thread.start_new_thread(exchange_loop, (client_socket, server_socket))
            _thread.start_new_thread(exchange_loop, (server_socket, client_socket))

if __name__ == '__main__':
    run()
