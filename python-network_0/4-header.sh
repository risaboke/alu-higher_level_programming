#!/bin/bash
# sends a GET request with a custom header and displays the body of the response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
