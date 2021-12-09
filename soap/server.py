import wsgiref.simple_server

from spyne import Application, Boolean, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Boolean, _returns=Unicode)
    def say_hello(self, name, enthusiastic):
        res = f"Hello {name}"
        if enthusiastic:
            res += "!"
        return res


def create_application():
    return Application(
        [HelloWorldService],
        tns="spyne.examples.hello",
        in_protocol=Soap11(validator="lxml"),
        out_protocol=Soap11(),
    )


class Server:
    def __init__(self, *, address, port):
        self.address = address
        self.port = port
        application = create_application()
        wsgi_app = WsgiApplication(application)
        self._wsgi_server = wsgiref.simple_server.make_server(
            address,
            port,
            wsgi_app,
        )

    @property
    def url(self):
        return f"http://{self.address}:{self.port}"

    @property
    def wsdl_url(self):
        return f"{self.url}?wsdl=1"

    def start(self):
        print("Server is listening on", self.url)
        self._wsgi_server.serve_forever()

    def stop(self):
        print("Shutting down server")
        self._wsgi_server.shutdown()


def main():
    server = Server(address="0.0.0.0", port=5678)
    server.start()


if __name__ == "__main__":
    main()
