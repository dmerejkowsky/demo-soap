# SOAP demo using Python

## Setup

* Install Python >= 3.9
* Install [poetry](https://python-poetry.org/)
* Install required dependencies:

```
$ poetry install
```

## Running the demo

```
# Start the server in a first shell
$ poetry run python soap/server.py

# Call the say_hello method from an
# other shell:
$ poetry run python soap/client.py
```

## What's in the repo

In `soap/client.py` - a SOAP client, written using the [zeep](https://docs.python-zeep.org/en/master/) library.

In `soap/server.py` - a SOAP server, written using [spyne](http://spyne.io).

In `./hello.wsdl`, the definition of the methods exposed by the demo server


## Running the linters and tests

```
$ poetry run invoke lint
$ poetry run pytest
```
