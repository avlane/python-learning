import contextlib
import io
import json
import os
import tempfile
import unittest

from exercises import todo


class TodoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = os.path.join(self.tmp.name, "todo.json")

    def run_cli(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = todo.main(["--file", self.path] + list(argv))
        return code, out.getvalue(), err.getvalue()

    def test_missing_file_is_an_empty_list(self):
        self.assertEqual(todo.load(self.path), [])

    def test_add_and_list(self):
        self.run_cli("add", "buy", "milk")
        self.run_cli("add", "call mum")
        code, out, _ = self.run_cli("list")
        self.assertEqual(code, 0)
        self.assertEqual(out.splitlines(), ["1. [ ] buy milk", "2. [ ] call mum"])

    def test_due_date_is_shown(self):
        self.run_cli("add", "--due", "2019-03-14", "pay rent")
        _, out, _ = self.run_cli("list")
        self.assertEqual(out.strip(), "1. [ ] pay rent (due 2019-03-14)")

    def test_list_by_due(self):
        self.run_cli("add", "no date")
        self.run_cli("add", "--due", "2019-05-01", "later")
        self.run_cli("add", "--due", "2019-04-01", "sooner")
        _, out, _ = self.run_cli("list", "--by-due")
        self.assertEqual(out.splitlines(), [
            "3. [ ] sooner (due 2019-04-01)",
            "2. [ ] later (due 2019-05-01)",
            "1. [ ] no date",
        ])

    def test_bad_due_date(self):
        code, _, err = self.run_cli("add", "--due", "tomorrow", "x")
        self.assertEqual(code, 1)
        self.assertIn("due date must look like", err)

    def test_done_is_saved(self):
        self.run_cli("add", "water plants")
        self.run_cli("done", "1")
        with open(self.path) as f:
            self.assertTrue(json.load(f)[0]["done"])

    def test_remove(self):
        self.run_cli("add", "one")
        self.run_cli("add", "two")
        code, out, _ = self.run_cli("remove", "1")
        self.assertEqual(out.strip(), "Removed: one")
        self.assertEqual([i["text"] for i in todo.load(self.path)], ["two"])

    def test_bad_number(self):
        self.run_cli("add", "one")
        code, _, err = self.run_cli("done", "5")
        self.assertEqual(code, 1)
        self.assertIn("there is no item 5", err)

    def test_corrupt_file_is_reported(self):
        with open(self.path, "w") as f:
            f.write("{not json")
        code, _, err = self.run_cli("list")
        self.assertEqual(code, 1)
        self.assertIn("is not valid JSON", err)

    def test_wrong_shape_is_reported(self):
        with open(self.path, "w") as f:
            f.write('{"a": 1}')
        code, _, err = self.run_cli("list")
        self.assertEqual(code, 1)
        self.assertIn("does not contain a list", err)

    def test_save_leaves_no_temp_file(self):
        self.run_cli("add", "x")
        self.assertEqual(os.listdir(self.tmp.name), ["todo.json"])

    def test_empty_list_message(self):
        _, out, _ = self.run_cli("list")
        self.assertEqual(out.strip(), "Nothing to do.")


if __name__ == "__main__":
    unittest.main()
