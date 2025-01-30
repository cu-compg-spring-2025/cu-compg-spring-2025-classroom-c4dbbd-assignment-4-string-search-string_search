import unittest
import string_search

class TestStringSearch(unittest.TestCase):
    def test_string_search(self):
        self.assertEqual(string_search.naive_search('abc', 'abc'), [0])
        self.assertEqual(string_search.naive_search('abcabc', 'abc'), [0,3])
        self.assertEqual(string_search.naive_search('abc', 'bc'), [1])
        self.assertEqual(string_search.naive_search('abc', 'c'), [2])
        self.assertEqual(string_search.naive_search('abc', 'x'), [])

if __name__ == '__main__':
    unittest.main()
