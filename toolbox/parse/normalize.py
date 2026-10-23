def clean_rows(rows):
    cleaned = []
    for row in rows:
        stripped = {}
        for key, value in row.items():
            text = "" if value is None else str(value).strip()
            stripped[key.strip().lower()] = text
        cleaned.append(stripped)
    return dedupe(cleaned)


def dedupe(rows):
    seen = set()
    unique = []
    for row in rows:
        marker = tuple(sorted(row.items()))
        if marker in seen:
            continue
        seen.add(marker)
        unique.append(row)
    return unique
