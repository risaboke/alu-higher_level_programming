# python-network_1

This project covers making HTTP requests from Python, first with the
built-in `urllib` package and then with the third-party `requests`
package: fetching a URL, reading response headers, sending `POST`
requests, handling HTTP errors, parsing JSON responses, and using
Basic Authentication against the GitHub API.

## Requirements

* All files are interpreted on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* Every file starts with `#!/usr/bin/python3`, ends with a new line, and is executable
* Code follows the `PEP 8` style (version 1.7)
* Every module has a documentation string
* Code is not executed on import (`if __name__ == "__main__":`)

## Tasks

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` with `urllib` and displays the response body |
| `1-hbtn_header.py` | Displays the `X-Request-Id` response header for a given URL, using `urllib` |
| `2-post_email.py` | Sends a `POST` request with an `email` parameter to a given URL, using `urllib` |
| `3-error_code.py` | Displays the response body for a URL, or `Error code: <status>` on an `HTTPError`, using `urllib` |
| `4-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` with `requests` and displays the response body |
| `5-hbtn_header.py` | Displays the `X-Request-Id` response header for a given URL, using `requests` |
| `6-post_email.py` | Sends a `POST` request with an `email` parameter to a given URL, using `requests` |
| `7-error_code.py` | Displays the response body for a URL, or `Error code: <status>` when the status is `>= 400`, using `requests` |
| `8-json_api.py` | Sends a `POST` request with a `q` letter parameter to `/search_user` and displays the resulting `id`/`name` |
| `10-my_github.py` | Displays a GitHub user's `id` using Basic Authentication against the GitHub API |

## Author

Lorna Ongesa
