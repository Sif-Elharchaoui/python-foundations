# Python Foundations

Small, focused Python programs written from scratch while learning the language,
as the first phase of my path into data engineering. Each folder covers one topic,
and each program solves a small, concrete problem rather than a textbook example.

## Contents

| Folder | Topic | Status |
|---|---|---|
| `01_variables_types/` | Variables, types, arithmetic, input, f-strings | Done |
| `02_conditionals/` | Conditions and boolean logic | Next |
| `03_loops/` | Loops and accumulation | Planned |
| `04_functions/` | Functions, scope, assertions | Planned |
| `05_strings_lists/` | Strings and lists | Planned |
| `06_dictionaries/` | Dictionaries, tuples, sets | Planned |

## 01 · Variables and types

| Program | What it does |
|---|---|
| `currency_converter.py` | Converts amounts between Chinese yuan and Moroccan dirham |
| `tutoring_invoice.py` | Builds an invoice for tutoring hours, after a platform fee |
| `file_size_converter.py` | Shows a byte count in KB, MB and GB |
| `duration_formatter.py` | Formats a duration in seconds as `h:mm:ss` |
| `api_rate_limit.py` | Works out how many hourly windows a batch of API requests needs |
| `storage_estimate.py` | Estimates raw and compressed storage for a stream of events |

## Running a program

Requires Python 3.12 or newer. From the repository root:

```bash
python3 01_variables_types/duration_formatter.py
```

## Conventions

- One program per file, named after what it does.
- Constants in `UPPER_CASE` at the top of each file; no unexplained numbers in formulas.
- Notes on each topic live in `docs/notes/`.
