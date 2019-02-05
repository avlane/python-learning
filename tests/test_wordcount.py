import os
import unittest

from exercises.wordcount import count_words

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "sample.txt")


class WordCountTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_words("a b a"), {"a": 2, "b": 1})

    def test_empty(self):
        self.assertEqual(count_words(""), {})

    def test_ignores_case_and_punctuation(self):
        self.assertEqual(count_words("The dog, the DOG!"), {"the": 2, "dog": 2})

    def test_keeps_apostrophes(self):
        self.assertEqual(count_words("it's here?"), {"it's": 1, "here": 1})

    def test_fixture_file(self):
        with open(FIXTURE) as f:
            counts = count_words(f.read())
        self.assertEqual(counts["fox"], 3)
        self.assertEqual(counts["the"], 4)
        self.assertEqual(counts["afternoon"], 2)


if __name__ == "__main__":
    unittest.main()
