from soap.client import Client


# Note: this calls a demo server that we do not control
# This will fail in case the demo server is not reachable
# when running the tests
def test_calling_add_integer():
    wsdl_url = "https://www.crcind.com/csp/samples/SOAP.Demo.cls?wsdl=1"
    client = Client(wsdl_url=wsdl_url)
    res = client.call("AddInteger", Arg1=1, Arg2=2)
    assert res == 3
