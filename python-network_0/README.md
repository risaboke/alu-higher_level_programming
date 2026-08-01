# python-network_0

This project covers making HTTP requests from the command line with
`curl`: inspecting response size and status code, retrieving the body
of a response, using different HTTP methods, sending custom headers,
sending `POST` parameters and JSON payloads, and following redirects.

## Requirements

* All scripts are tested on Ubuntu 20.04 LTS
* Every script is exactly 3 lines long (`wc -l file`)
* Every script starts with `#!/bin/bash`, ends with a new line, and is executable
* The second line of every script is a comment explaining what it does
* Every `curl` command uses the `-s` (silent) option

## Tasks

| File | Description |
| --- | --- |
| `0-body_size.sh` | Sends a request to a URL and displays the size in bytes of the response body |
| `1-body.sh` | Sends a `GET` request to a URL and displays the body of the response, only if the status code is `200` |
| `2-delete.sh` | Sends a `DELETE` request to a URL and displays the body of the response |
| `3-methods.sh` | Displays all the HTTP methods a server accepts for a given URL |
| `4-header.sh` | Sends a `GET` request with an `X-HolbertonSchool-User-Id` header and displays the body of the response |
| `5-post_params.sh` | Sends a `POST` request with `email` and `subject` parameters and displays the body of the response |
| `100-status_code.sh` | Sends a request to a URL and displays only the status code of the response |
| `101-post_json.sh` | Sends a `POST` request with the contents of a file as the JSON body and displays the response |
| `102-catch_me.sh` | Sends a request to `/catch_me` and displays the `"You got me!"` response |

## Author

Lorna Ongesa
