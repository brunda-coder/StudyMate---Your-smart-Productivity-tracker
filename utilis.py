import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        return{}
    with open (file_path, 'r') as file:
        return json.load(f)
       
def save_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok = True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
        