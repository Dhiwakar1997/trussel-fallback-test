REQUIRED_FIELDS = ("name", "email")


def validate(rows):
    valid = []
    for row in rows:
        missing = [field for field in REQUIRED_FIELDS if not row.get(field)]
        if missing:
            continue
        valid.append(row)
    return valid
