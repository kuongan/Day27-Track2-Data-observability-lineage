import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.validation import read_rows, build_summary

DATA_DIR = PROJECT_ROOT / "data"


class TestValidationSummary(unittest.TestCase):
    def test_passed_dataset(self):
        rows = read_rows(DATA_DIR / "orders_passed.csv")
        summary = build_summary(rows)
        self.assertEqual(summary["validation_status"], "passed")
        self.assertEqual(summary["missing_customer_ids"], 0)
        self.assertEqual(summary["invalid_amounts"], 0)
        self.assertEqual(summary["invalid_statuses"], 0)

    def test_failed_dataset(self):
        rows = read_rows(DATA_DIR / "orders_failed.csv")
        summary = build_summary(rows)
        self.assertEqual(summary["validation_status"], "failed")
        self.assertGreater(summary["missing_customer_ids"], 0)
        self.assertGreater(summary["invalid_amounts"], 0)
        self.assertGreater(summary["invalid_statuses"], 0)


if __name__ == "__main__":
    unittest.main()
