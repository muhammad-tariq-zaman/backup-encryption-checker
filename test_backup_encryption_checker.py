import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check

def row(b, enc, key):
    return {"backup": b, "encrypted": enc, "key_id": key}

class TestEncryption(unittest.TestCase):
    def test_encrypted(self):
        self.assertEqual(check([row("B1", "yes", "K1")])[0][1], "ENCRYPTED")
    def test_key_missing(self):
        self.assertEqual(check([row("B1", "yes", "")])[0][1], "KEY MISSING")
    def test_unencrypted(self):
        self.assertEqual(check([row("B1", "no", "")])[0][1], "UNENCRYPTED")
    def test_key_without_encryption_still_unencrypted(self):
        self.assertEqual(check([row("B1", "no", "K1")])[0][1], "UNENCRYPTED")
