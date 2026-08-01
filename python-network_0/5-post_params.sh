#!/bin/bash
# sends a POST request with email and subject parameters and displays the response body
curl -s -X POST --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
