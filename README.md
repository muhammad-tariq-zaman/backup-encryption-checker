# backup-encryption-checker

Audit backup jobs for encryption: encrypted with a key, encrypted but key missing, or plain unencrypted — the last two are the ones to fix first.

## How to run

```sh
python3 main.py backups.csv
```

## Example output

```
DB-nightly: ENCRYPTED
Files-weekly: UNENCRYPTED
1 backup(s) not safely encrypted.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
