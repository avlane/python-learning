import sys


def count_words(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def main():
    if len(sys.argv) != 2:
        print("usage: python3 -m exercises.wordcount FILE")
        return
    with open(sys.argv[1]) as f:
        counts = count_words(f.read())
    for word in sorted(counts, key=counts.get, reverse=True):
        print(counts[word], word)


if __name__ == "__main__":
    main()
