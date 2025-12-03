#!/usr/bin/python3
import urllib

def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    content = fetch_url(url)
    print(content)
