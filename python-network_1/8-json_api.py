#!/usr/bin/python3
"""Send a POST request to the search_user endpoint with a letter parameter."""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
