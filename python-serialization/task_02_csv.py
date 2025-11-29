#!/usr/bin/env python3
"""Convert a CSV file to a JSON file."""

import csv
import json

def convert_csv_to_json(csv_filename, json_filename="data.json"):
    """
    Convert CSV data to JSON and save it to a file.

    :param csv_filename: Input CSV file
    :param json_filename: Output JSON file (default: data.json)
    :return: True if conversion succeeded, False otherwise
    """
    try:
        data = []
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error, json.JSONDecodeError):
        return False

