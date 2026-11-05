"""Check backup jobs for encryption coverage.

Usage: python3 main.py backups.csv
CSV columns: backup,encrypted (yes/no),key_id.
ENCRYPTED only when encrypted=yes and a key id is present;
encrypted=yes with no key is KEY MISSING; encrypted=no is
UNENCRYPTED.
"""
import argparse, csv, sys

def check(rows):
    out = []
    for row in rows:
        encrypted = row["encrypted"].strip().lower() == "yes"
        key = row["key_id"].strip()
        if encrypted and key:
            verdict = "ENCRYPTED"
        elif encrypted:
            verdict = "KEY MISSING"
        else:
            verdict = "UNENCRYPTED"
        out.append((row["backup"], verdict))
    return out

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        result = check(list(csv.DictReader(f)))
    bad = sum(1 for _, v in result if v != "ENCRYPTED")
    for backup, verdict in result:
        print(f"{backup}: {verdict}")
    print(f"{bad} backup(s) not safely encrypted.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
