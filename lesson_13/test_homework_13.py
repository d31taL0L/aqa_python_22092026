import unittest
from homework_10 import log_event


class TestLogEventPositive(unittest.TestCase):
    def test_success_status_logs_info(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "success")
        self.assertEqual(captured_logs.records[0].levelname, "INFO")

    def test_expired_status_logs_warning(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "expired")
        self.assertEqual(captured_logs.records[0].levelname, "WARNING")

    def test_failed_status_logs_error(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "failed")
        self.assertEqual(captured_logs.records[0].levelname, "ERROR")

    def test_username_in_log_message(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "success")
        self.assertIn("John", captured_logs.output[0])


class TestLogEventNegative(unittest.TestCase):
    def test_unknown_status_logs_error(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "abc")
        self.assertEqual(captured_logs.records[0].levelname, "ERROR")

    def test_uppercase_status_logs_error(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "SUCCESS")
        self.assertEqual(captured_logs.records[0].levelname, "ERROR")

    def test_empty_status_logs_error(self):
        with self.assertLogs("log_event", level="INFO") as captured_logs:
            log_event("John", "")
        self.assertEqual(captured_logs.records[0].levelname, "ERROR")


if __name__ == "__main__":
    unittest.main()