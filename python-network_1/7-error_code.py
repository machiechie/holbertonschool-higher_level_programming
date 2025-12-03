#!/usr/bin/python3
"""Fetches a URL and handles HTTP status codes >= 400"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
