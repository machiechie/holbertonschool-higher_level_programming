#!/usr/bin/python3
"""Fetches the X-Request-Id header from a URL"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))
