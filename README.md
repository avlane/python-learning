# python-learning

Small exercises I write while learning Python 3. Nothing here is clever; it is mostly practice.
Needs Python 3.6 or newer and nothing outside the standard library.

## Exercises

| module | what it does | run it |
|---|---|---|
| `exercises/hello.py` | greets you | `python3 -m exercises.hello` |
| `exercises/guessing_game.py` | guess a number from 1 to 100 | `python3 -m exercises.guessing_game` |
| `exercises/temperature.py` | Celsius and Fahrenheit converter | `python3 -m exercises.temperature` |
| `exercises/fizzbuzz.py` | the classic | `python3 -m exercises.fizzbuzz` |
| `exercises/wordcount.py` | count words in a text file | `python3 -m exercises.wordcount tests/fixtures/sample.txt --top 5` |
| `exercises/todo.py` | todo list kept in a JSON file | `python3 -m exercises.todo add --due 2019-04-01 pay rent` |
| `exercises/tictactoe.py` | two player game, or `--computer` | `python3 -m exercises.tictactoe --computer` |
| `exercises/primes.py` | sieve of Eratosthenes | `python3 -m exercises.primes 50` |

The todo list is stored in `~/.todo.json`; use `--file PATH` or the `TODO_FILE` environment variable to put it elsewhere.

## todo data file

The file is a JSON list. Each item looks like this:

```json
{"text": "pay rent", "done": false, "due": "2019-04-01"}
```

`due` is `null` when no date was given.

## Tests

```
python3 -m unittest discover
```