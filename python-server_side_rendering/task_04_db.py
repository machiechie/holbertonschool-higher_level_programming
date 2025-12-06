# task_04_db.py
import sqlite3
import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)
DATABASE = 'products.db'
JSON_FILE = 'products.json'

# --- Data Fetching Functions ---

def get_data_from_json():
    """Reads product data from a JSON file."""
    try:
        if not os.path.exists(JSON_FILE):
            print(f"Error: JSON file '{JSON_FILE}' not found.")
            return []
            
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON reading error: {e}")
        return []

def get_data_from_csv():
    """Reads product data from a CSV file (assuming 'products.csv' exists or using mock data)."""
    # Using mock data structure similar to previous tasks for consistency
    csv_data = [
        ['id', 'name', 'category', 'price'],
        ['201', 'Book', 'Media', '12.99'],
        ['202', 'Pen', 'Office Supplies', '3.50']
    ]
    
    header = csv_data[0]
    products = []
    for row in csv_data[1:]:
        # Create dictionary from CSV rows
        products.append(dict(zip(header, row)))
    return products

def get_data_from_db():
    """Fetches product data from the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        # Configure connection to return rows as dictionaries for easier template handling
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        
        # Convert sqlite3.Row objects to standard dictionaries
        products = [dict(row) for row in rows]
        return products
    except sqlite3.Error as e:
        # Handle database connection or query errors
        print(f"Database error: {e}")
        return None  # Return None to signal a critical error
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# --- Flask Route ---

@app.route('/products')
def product_display():
    source = request.args.get('source')
    products = None
    error_message = None

    if source == 'json':
        products = get_data_from_json()
    elif source == 'csv':
        products = get_data_from_csv()
    elif source == 'sql':
        products = get_data_from_db()
        if products is None:
            # Database connection/read failed
            error_message = "Database Error: Could not retrieve data."
    else:
        # Invalid source parameter
        error_message = "Wrong source. Please use 'json', 'csv', or 'sql'."

    if error_message:
        return render_template('product_display.html', error=error_message)
    elif products is not None:
        return render_template('product_display.html', products=products, source=source)
    else:
        # Fallback for unexpected case
        return render_template('product_display.html', error="An unknown error occurred.")

if __name__ == '__main__':
    # Ensure the database is set up before running the app
    import db_setup
    db_setup.create_database()
    app.run(debug=True)
