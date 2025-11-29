#!/usr/bin/env python3
"""Convert a CSV file to a JSON file."""


import csv
import json

def convert_csv_to_json(csv_filename, json_filename):
    data = []
    
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
