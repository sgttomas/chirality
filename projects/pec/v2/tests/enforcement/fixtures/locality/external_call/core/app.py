import socket


def notify() -> None:
    socket.create_connection(("198.51.100.10", 443))
