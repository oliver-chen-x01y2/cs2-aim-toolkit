import json
def load_config(path):
    with open(path, 'r') as f:
        return json.load(f)