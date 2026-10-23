import os


def write_report(rows, path):
    folder = os.path.dirname(os.path.abspath(path))
    os.makedirs(folder, exist_ok=True)
    text = "\n".join(rows) + "\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path
