#!/usr/bin/python3
"""Display your GitHub id using Basic Authentication with the GitHub API."""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get("https://api.github.com/user",
                             auth=(username, password))
    print(response.json().get("id"))
