import argparse
import re
from collections import Counter

WORD_RE = re.compile(r"[a-z0-9']+")
STOP_WORDS = frozenset("a an and are as at be but by for if in is it its of on or so the to was with".split())


def count_words(text, skip_common=False):
    """Count words, ignoring case and punctuation."""
    words = WORD_RE.findall(text.lower())
    if skip_common:
        words = [w for w in words if w not in STOP_WORDS]
    return Counter(words)


def top_words(counts, n=None):
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked if n is None else ranked[:n]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Count the words in a text file.")
    parser.add_argument("file")
    parser.add_argument("--top", type=int, metavar="N", help="only show the N most common words")
    parser.add_argument("--skip-common", action="store_true", help="leave out words like 'the' and 'and'")
    args = parser.parse_args(argv)
    with open(args.file) as f:
        counts = count_words(f.read(), args.skip_common)
    for word, n in top_words(counts, args.top):
        print(n, word)


if __name__ == "__main__":
    main()
