#!/usr/bin/env python3
"""
Task 04 – Dynamic Data Display + SQLite
Flask app that displays product data from JSON, CSV, or SQLite.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def load_from_json():
    """Load products from a JSON file."""
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except Exception:
        return None


def load_from_csv():
    """Load products from a CSV file."""
    try:
        products = []
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": row["id"],
                    "name": row["name"],
                    "category": row["category"],
                    "price": row["price"]
                })
        return products
    except Exception:
        return None


def load_from_sqlite():
    """Load products from SQLite database."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3],
            })

        conn.close()
        return products

    except Exception:
        return None


@app.route("/")
def display_products():
    source = request.args.get("source")

    if source == "json":
        data = load_from_json()

    elif source == "csv":
        data = load_from_csv()

    elif source == "sql":
        data = load_from_sqlite()

    else:
        return render_template("product_display.html",
                               error="Wrong source",
                               products=None)

    # If database / file error
    if data is None:
        return render_template("product_display.html",
                               error="Error loading data",
                               products=None)

    return render_template("product_display.html", products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True)
