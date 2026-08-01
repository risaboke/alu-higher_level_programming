#!/bin/bash
# sends a request to /catch_me with a browser-like User-Agent to get "You got me!"
curl -s -L -A "Mozilla/5.0" "0.0.0.0:5000/catch_me"
