#!/usr/bin/python3
"""Displays your GitHub id using Basic Authentication"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, token)
    )

    if response.status_code == 200:
        data = response.json()
        print(data.get("id"))
    else:
        print("Error: {}".format(response.status_code))
