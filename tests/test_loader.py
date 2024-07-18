# tests/test_loader.py

import unittest
from wikifunctions.loader import WikiFunctionLoader

class TestWikiFunctionLoader(unittest.TestCase):
    def test_execute_function(self):
        loader = WikiFunctionLoader("Z12774")
        result = loader.execute_function("80", "1.8")
        self.assertIsNotNone(result)

    def test_fetch_description(self):
        loader = WikiFunctionLoader("Z12774")
        description = loader.fetch_description()
        self.assertIsNotNone(description)

if __name__ == '__main__':
    unittest.main()
