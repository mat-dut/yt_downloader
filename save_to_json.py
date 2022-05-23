from fileinput import filename
import json


def save_to_json(fileName, data):
    with open('data.json', 'w') as f:
        json.dump(data, f)
