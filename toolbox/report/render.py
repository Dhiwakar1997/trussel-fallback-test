def summarize(rows):
    count = len(rows)
    fields = sorted({key for row in rows for key in row})
    return {"count": count, "fields": fields}


def render_html(rows):
    summary = summarize(rows)
    lines = ["<html>", "<body>", f"<p>{summary['count']} rows</p>", "<ul>"]
    for field in summary["fields"]:
        lines.append(f"<li>{field}</li>")
    lines.extend(["</ul>", "</body>", "</html>"])
    return lines
