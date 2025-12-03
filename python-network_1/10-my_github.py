#!/usr/bin/python3
"""Displays your GitHub id using Basic Authentication"""

import sys
import requests
import os

if __name__ == "__main__":
    username = sys.argv[1]
    token = os.environ.get("GITHUB_TOKEN")  # do not hardcode

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, token)
    )

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print("Error: {}".format(response.status_code))

