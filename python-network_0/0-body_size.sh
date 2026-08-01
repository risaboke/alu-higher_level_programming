#!/bin/bash
# sends a request to a URL and displays the size in bytes of the response body
curl -s -o /dev/null -w "%{size_download}\n" "$1"
