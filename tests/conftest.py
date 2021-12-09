import socket
import threading

import pytest

from soap.server import Server


@pytest.fixture
def free_port():
    """Tries to find a free port by listening
    to port 0 and returning the port that was
    randomly assigned by the OS.

    It's possible this will fail, but it's very
    unlikely
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 0))
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.fixture
def server(free_port):
    server = Server(address="0.0.0.0", port=free_port)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()
    yield server
    print("shuting down server")
    server.stop()
    server_thread.join()
