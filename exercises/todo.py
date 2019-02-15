import argparse
import json
import os
import sys

DEFAULT_PATH = os.path.expanduser("~/.todo.json")


def load(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


def save(path, items):
    with open(path, "w") as f:
        json.dump(items, f, indent=2)


def add(items, text):
    items.append({"text": text, "done": False})
    return items


def format_items(items):
    if not items:
        return "Nothing to do."
    lines = []
    for number, item in enumerate(items, 1):
        mark = "x" if item["done"] else " "
        lines.append("{}. [{}] {}".format(number, mark, item["text"]))
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="A tiny todo list stored in a JSON file.")
    parser.add_argument("--file", default=os.environ.get("TODO_FILE", DEFAULT_PATH))
    sub = parser.add_subparsers(dest="command")
    sub.required = True
    p_add = sub.add_parser("add", help="add an item")
    p_add.add_argument("text", nargs="+")
    sub.add_parser("list", help="show all items")
    args = parser.parse_args(argv)

    items = load(args.file)
    if args.command == "add":
        add(items, " ".join(args.text))
        save(args.file, items)
        print("Added.")
    elif args.command == "list":
        print(format_items(items))


if __name__ == "__main__":
    main()
