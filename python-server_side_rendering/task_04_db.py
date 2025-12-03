from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Функция для чтения JSON
def read_json():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        return data, None
    except Exception as e:
        return [], f"Error reading JSON: {e}"

# Функция для чтения CSV
def read_csv():
    try:
        data = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Преобразуем цену в float
                row['price'] = float(row['price'])
                data.append(row)
        return data, None
    except Exception as e:
        return [], f"Error reading CSV: {e}"

# Функция для чтения из SQLite
def read_sqlite():
    try:
        if not os.path.exists('products.db'):
            return [], "Database file not found"
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        data = []
        for r in rows:
            data.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
        conn.close()
        return data, None
    except Exception as e:
        return [], f"Database error: {e}"

@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    prod_id = request.args.get('id', None)
    
    if source == 'json':
        data, error = read_json()
    elif source == 'csv':
        data, error = read_csv()
    elif source == 'sql':
        data, error = read_sqlite()
    else:
        return render_template('product_display.html', products=[], error="Wrong source")

    if error:
        return render_template('product_display.html', products=[], error=error)

    # Фильтрация по id
    if prod_id:
        try:
            prod_id = int(prod_id)
            filtered = [p for p in data if p['id'] == prod_id]
            if not filtered:
                return render_template('product_display.html', products=[], error="Product not found")
            data = filtered
        except ValueError:
            return render_template('product_display.html', products=[], error="Invalid id")

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

