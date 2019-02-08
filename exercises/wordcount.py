import argparse
import re
from collections import Counter

WORD_RE = re.compile(r"[a-z0-9']+")


def count_words(text):
    """Count words, ignoring case and punctuation."""
    return Counter(WORD_RE.findall(text.lower()))


def top_words(counts, n=None):
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked if n is None else ranked[:n]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Count the words in a text file.")
    parser.add_argument("file")
    parser.add_argument("--top", type=int, metavar="N", help="only show the N most common words")
    args = parser.parse_args(argv)
    with open(args.file) as f:
        counts = count_words(f.read())
    for word, n in top_words(counts, args.top):
        print(n, word)


if __name__ == "__main__":
    main()
