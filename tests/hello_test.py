import unittest
import hello


class TestHello(unittest.TestCase):
    """Test case for hello package"""

    def test_hello(self):
        """default argument"""

        self.assertEqual("Hello World", hello.greeting())

    def test_hello_arg(self):
        """with argument"""
        self.assertEqual("Hello Everybody", hello.greeting("Everybody"))


if __name__ == "__main__":
    unittest.main()
