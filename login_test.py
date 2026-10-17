import unittest


def validate_login(username, password):
    return bool(username.strip()) and bool(password.strip())


class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        self.assertTrue(validate_login("student01", "ValidPass123"))

    def test_empty_username(self):
        self.assertFalse(validate_login("", "ValidPass123"))

    def test_empty_password(self):
        self.assertFalse(validate_login("student01", ""))

    def test_whitespace_username(self):
        self.assertFalse(validate_login("   ", "ValidPass123"))


if __name__ == "__main__":
    unittest.main()