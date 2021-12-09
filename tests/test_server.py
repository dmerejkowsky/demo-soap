import requests
from lxml import etree


def test_wsdl_is_up_to_date(server):
    """Check that the source code of our SOAP service
    matches the expected schema

    The purpose of this test is to let us know whenever
    we break our server API
    """
    response = requests.get(server.wsdl_url)
    actual_xml = response.text

    actual_doc = etree.fromstring(actual_xml.encode())
    actual_tree = etree.ElementTree(actual_doc)
    actual_xml = etree.tostring(actual_tree, pretty_print=True).decode()
    actual_xml = actual_xml.replace(str(server.port), "5678")

    with open("hello.wsdl", "r") as f:
        expected_xml = f.read()

    assert actual_xml == expected_xml
