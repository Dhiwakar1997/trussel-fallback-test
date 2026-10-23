import argparse

from toolbox.io.readers import read_csv
from toolbox.io.writers import write_report
from toolbox.parse.normalize import clean_rows
from toolbox.parse.schema import validate
from toolbox.report.render import render_html


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Clean a CSV and write an HTML report.")
    parser.add_argument("source", help="input CSV file")
    parser.add_argument("output", help="HTML file to write")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    rows = read_csv(args.source)
    rows = clean_rows(rows)
    rows = validate(rows)
    lines = render_html(rows)
    write_report(lines, args.output)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
