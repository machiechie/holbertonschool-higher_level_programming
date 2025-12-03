#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print status code + titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # print status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save id/title/body to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # build list of dictionaries
        posts_list = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in data
        ]

        # write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_list)
