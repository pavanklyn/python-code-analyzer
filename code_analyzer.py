import ast
import sys


def analyze_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()
    except OSError as e:
        print(f"Error reading file: {e}")
        return

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Syntax error in file: {e}")
        return

    imports, functions, classes = set(), set(), set()
    variables, calls = set(), set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ''
            for alias in node.names:
                name = f"{module}.{alias.name}" if module else alias.name
                imports.add(name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.add(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables.add(target.id)
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.add(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.add(node.func.attr)

    print("\nPYTHON CODE ANALYSIS")
    print("=" * 22)
    print(f"File: {path}")
    print(f"Total lines: {len(source.splitlines())}")
    print(f"Imports ({len(imports)}): {', '.join(sorted(imports)) or 'None'}")
    print(f"Functions ({len(functions)}): {', '.join(sorted(functions)) or 'None'}")
    print(f"Classes ({len(classes)}): {', '.join(sorted(classes)) or 'None'}")
    print(f"Variables ({len(variables)}): {', '.join(sorted(variables)) or 'None'}")
    print(f"Function calls ({len(calls)}): {', '.join(sorted(calls)) or 'None'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python code_analyzer.py <path_to_python_file>")
    else:
        analyze_file(sys.argv[1])
