from soap.client import Client


def test_calling_own_server(server):
    client = Client(wsdl_url=server.wsdl_url)
    res = client.call("say_hello", name="world", enthusiastic=True)
    assert res == "Hello world!"
