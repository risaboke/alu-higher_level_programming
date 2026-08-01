#!/bin/bash
# sends a GET request to a URL and displays the body only when the status code is 200
code=$(curl -s -o /tmp/1-body_$$ -w "%{http_code}" "$1"); [ "$code" = "200" ] && cat /tmp/1-body_$$; rm -f /tmp/1-body_$$
