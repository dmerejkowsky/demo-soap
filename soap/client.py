from zeep import Client as ZeepClient


class Client:
    def __init__(self, *, wsdl_url):
        self._zeep_client = ZeepClient(wsdl_url)

    def call(self, method, **kwargs):
        service = self._zeep_client.service
        method = getattr(service, method)
        return method(**kwargs)


def main():
    client = Client(wsdl_url="http://localhost:5678?wsdl=1")
    res = client.call("say_hello", name="world", enthusiastic=True)
    print(res)


if __name__ == "__main__":
    main()
