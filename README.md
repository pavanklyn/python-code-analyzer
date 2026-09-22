# Analyze Python Code Automatically

A quick static-analysis mini project that summarizes a Python file's
imports, functions, classes, variables, and function calls using the
built-in `ast` module — no code execution involved.

## Files

- `code_analyzer.py` — the analyzer script
- `example.py` — a sample Python file to try it on

## How to run

```bash
python code_analyzer.py example.py
```

## Sample output

```
PYTHON CODE ANALYSIS
======================
File: example.py
Total lines: 22
Imports (2): datetime.datetime, math
Functions (3): __init__, calculate_area, main
Classes (1): Circle
Variables (3): area, pi, today
Function calls (5): calculate_area, main, now, print, round
```

## Notes

- Performs static analysis only (does not run the code).
- Uses only the standard Python library — no extra installation needed.
- Detects simple variable assignments (not function parameters).

## Useful for

- Quick code reviews
- Learning from existing projects
- Understanding code structure
