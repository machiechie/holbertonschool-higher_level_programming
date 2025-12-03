from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        return json.load(f)

def read_csv(file_path):
    if not os.path.exists(file_path):
        return []
    data = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # преобразуем price и id в числа
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    # выбираем источник данных
    if source == 'json':
        products_list = read_json('products.json')
    elif source == 'csv':
        products_list = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # фильтруем по id, если задан
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Invalid id", products=[])
        filtered = [p for p in products_list if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        products_list = filtered

    return render_template('product_display.html', products=products_list, error=None)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
