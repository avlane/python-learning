import argparse
import json
import datetime
import os
import sys

DEFAULT_PATH = os.path.expanduser("~/.todo.json")


class TodoError(Exception):
    pass


def _check_number(items, number):
    if not 1 <= number <= len(items):
        raise TodoError("there is no item {} (the list has {})".format(number, len(items)))


def load(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        try:
            items = json.load(f)
        except ValueError:
            raise TodoError("{} is not valid JSON; fix or delete it".format(path))
    if not isinstance(items, list):
        raise TodoError("{} does not contain a list of items".format(path))
    return items


def save(path, items):
    # write to a temporary file first so a crash cannot leave half a file behind
    tmp_path = path + ".tmp"
    with open(tmp_path, "w") as f:
        json.dump(items, f, indent=2)
    os.replace(tmp_path, path)


def validate_due(due):
    """Return the due date as YYYY-MM-DD; accepts 2019-3-5 and fixes it up."""
    if due is None:
        return None
    try:
        return datetime.datetime.strptime(due, "%Y-%m-%d").date().isoformat()
    except ValueError:
        raise TodoError("due date must look like 2019-03-14, got {!r}".format(due))


def add(items, text, due=None):
    items.append({"text": text, "done": False, "due": validate_due(due)})
    return items


def mark_done(items, number):
    _check_number(items, number)
    items[number - 1]["done"] = True
    return items


def remove(items, number):
    _check_number(items, number)
    return items.pop(number - 1)


def format_items(items, by_due=False):
    if not items:
        return "Nothing to do."
    numbered = list(enumerate(items, 1))
    if by_due:
        # items without a due date go last; numbers still refer to the stored order
        numbered.sort(key=lambda pair: (not pair[1].get("due"), pair[1].get("due") or ""))
    lines = []
    for number, item in numbered:
        mark = "x" if item["done"] else " "
        line = "{}. [{}] {}".format(number, mark, item["text"])
        if item.get("due"):
            line += " (due {})".format(item["due"])
        lines.append(line)
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="A tiny todo list stored in a JSON file.")
    parser.add_argument("--file", default=os.environ.get("TODO_FILE", DEFAULT_PATH))
    sub = parser.add_subparsers(dest="command")
    sub.required = True
    p_add = sub.add_parser("add", help="add an item")
    p_add.add_argument("text", nargs="+")
    p_add.add_argument("--due", metavar="YYYY-MM-DD")
    p_list = sub.add_parser("list", help="show all items")
    p_list.add_argument("--by-due", action="store_true", help="show the earliest due date first")
    p_done = sub.add_parser("done", help="mark an item as done")
    p_done.add_argument("number", type=int)
    p_rm = sub.add_parser("remove", help="delete an item")
    p_rm.add_argument("number", type=int)
    args = parser.parse_args(argv)

    try:
        items = load(args.file)
        if args.command == "add":
            add(items, " ".join(args.text), args.due)
            save(args.file, items)
            print("Added.")
        elif args.command == "done":
            mark_done(items, args.number)
            save(args.file, items)
            print("Marked item {} as done.".format(args.number))
        elif args.command == "remove":
            removed = remove(items, args.number)
            save(args.file, items)
            print("Removed: {}".format(removed["text"]))
        elif args.command == "list":
            print(format_items(items, args.by_due))
    except TodoError as err:
        print("todo: {}".format(err), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
