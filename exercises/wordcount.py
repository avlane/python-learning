import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[a-z0-9']+")


def count_words(text):
    """Count words, ignoring case and punctuation."""
    return Counter(WORD_RE.findall(text.lower()))


def main():
    if len(sys.argv) != 2:
        print("usage: python3 -m exercises.wordcount FILE")
        return
    with open(sys.argv[1]) as f:
        counts = count_words(f.read())
    for word, n in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(n, word)


if __name__ == "__main__":
    main()
