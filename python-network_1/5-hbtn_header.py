#!/usr/bin/python3
"""Display the value of the X-Request-Id header from a URL's response."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
