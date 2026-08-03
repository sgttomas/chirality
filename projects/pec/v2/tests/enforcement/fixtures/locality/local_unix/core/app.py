import socket


def connect_local() -> None:
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect("/tmp/pec-v2.sock")
