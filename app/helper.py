import json


def json_reader(file):
    with open(file, 'r') as fp:
        raw = fp.read()
    data = json.loads(raw)
    return data
