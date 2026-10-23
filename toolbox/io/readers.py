import csv
import json


def read_csv(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(dict(row))
    return rows


def read_json(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        data = [data]
    return list(data)


def read_unused(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    lines = raw.decode("utf-8").splitlines()
    cleaned = [line.strip() for line in lines]
    non_blank = [line for line in cleaned if line]
    return non_blank
