import socket


def connect_local() -> None:
    socket.create_connection(("127.0.0.1", 8765))
