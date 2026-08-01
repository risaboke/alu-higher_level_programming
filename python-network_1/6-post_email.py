#!/usr/bin/python3
"""Send a POST request to a URL with an email parameter and print the body."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={"email": email})
    print(response.text)
