# Day 1 reference: values, types and computation

Source: lesson from my tutor, 12 October 2026.

## 1. How Python runs code
- `python3 file.py` runs the file from top to bottom. No `main` method is needed.
- An error stops the program at that line; earlier lines have already run.
- `python3` alone opens the REPL, where each expression's value prints automatically.

## 2. Variables are names
- `x = 5` makes the name `x` point to the object `5`. The object has the type, not the name.
- Names can later point to another type (dynamic typing), so clear names matter.
- Numbers and strings are immutable: `y = x; y += 1` leaves `x` unchanged.

## 3. Core types

| Type | Example | Note |
|---|---|---|
| `int` | `42`, `2**100` | No size limit |
| `float` | `3.14`, `1e3` | 64-bit binary floating point, not exact |
| `str` | `"hello"` | Text, immutable |
| `bool` | `True`, `False` | Subclass of `int`: `True + True == 2` |
| `None` | `None` | No value |

## 4. Arithmetic

| Operator | `7 ? 2` | Note |
|---|---|---|
| `/` | `3.5` | Always returns a float |
| `//` | `3` | Floor division, rounds toward minus infinity: `-7 // 2 == -4` |
| `%` | `1` | Remainder; `a == (a // b) * b + a % b` |
| `**` | `49` | Power |

Precedence: `**`, then `* / // %`, then `+ -`. Use brackets when unsure.

Splitting a quantity into units:

```python
total = 125
minutes = total // 60   # 2
seconds = total % 60    # 5
```

## 5. Floats are approximations
```python
0.1 + 0.2        # 0.30000000000000004
round(2.675, 2)  # 2.67
```
- Format for display (`:.2f`); never compare floats with `==`.
- Real money uses `decimal.Decimal` or integer minor units (fen, cents).

## 6. Type conversion

| Call | Result | Fails when |
|---|---|---|
| `int("42")` | `42` | Not a whole number: `int("4.2")` → `ValueError` |
| `float("4.2")` | `4.2` | Not a number |
| `int(4.9)` | `4` | Never; it truncates, it does not round |
| `str(42)` | `"42"` | Never |

Rule: data from outside the program arrives as text. Convert it where you read it.

## 7. Input and output
```python
name = input("Student: ")
hours = int(input("Hours: "))
print("-" * 30)
```

## 8. f-string format specs

| Spec | Example | Result |
|---|---|---|
| `.2f` | `f"{3.14159:.2f}"` | `3.14` |
| `,.2f` | `f"{1234567.891:,.2f}"` | `1,234,567.89` |
| `02d` | `f"{7:02d}"` | `07` |
| `.1%` | `f"{0.256:.1%}"` | `25.6%` |
| `>8` | `f"{42:>8}"` | `      42` |

## 9. Style
- `snake_case` for variables, `UPPER_CASE` for constants.
- Put units in names: `size_bytes`, `duration_seconds`.
- No magic numbers in formulas: `PLATFORM_FEE_RATE = 0.10`.
- Order in a script: constants, input, computation, output.

## 10. Reading errors
Read the traceback from the bottom: last line says what, the line above says where.

| Error | Usual cause |
|---|---|
| `NameError` | Typo, or name used before assignment |
| `TypeError` | Wrong types for the operation, often a missing `float()` |
| `ValueError` | Right type, unusable value: `int("abc")` |
| `SyntaxError` | Missing bracket, quote or colon |

## 11. Workflow for each program
1. Write the spec as comments: input, compute, output, one expected example.
2. Code one section at a time, running after each.
3. Compare with the expected output character by character.
4. Test a boundary case: zero, very large, an exact multiple.
5. Commit with a message that says what changed.