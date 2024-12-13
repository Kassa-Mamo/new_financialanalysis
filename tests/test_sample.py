import unittest

class TestSample(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3  # Example of the code you're testing
        expected_result = 5
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
