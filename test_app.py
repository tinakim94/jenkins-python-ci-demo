import unittest
from app import add, get_status


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 6)

    def test_status(self):
        self.assertEqual(
            get_status(),
            "Jenkins pipeline is running!"
        )


if __name__ == "__main__":
    unittest.main()