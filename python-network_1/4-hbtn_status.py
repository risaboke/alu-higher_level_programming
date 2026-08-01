#!/usr/bin/python3
"""Fetch https://alu-intranet.hbtn.io/status and display the response body."""
import requests

if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
