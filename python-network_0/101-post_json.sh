#!/bin/bash
# sends a POST request with a JSON file as the body and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
