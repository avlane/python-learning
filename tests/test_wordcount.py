import os
import unittest

from exercises.wordcount import count_words

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "sample.txt")


class WordCountTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_words("a b a"), {"a": 2, "b": 1})

    def test_empty(self):
        self.assertEqual(count_words(""), {})

    def test_fixture_file(self):
        with open(FIXTURE) as f:
            counts = count_words(f.read())
        self.assertEqual(counts["fox"], 2)
        self.assertEqual(counts["afternoon"], 1)


if __name__ == "__main__":
    unittest.main()
