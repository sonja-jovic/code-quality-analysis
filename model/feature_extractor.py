import ast
from radon.complexity import cc_visit

def extract_features(code: str):

    # Split the code into individual lines
    lines = code.split("\n")

    # Feature 1: Lines of code
    # Measures the size of the code
    loc = len(lines)

    # Feature 2: Number of comment lines
    # We check if a line starts with "#"
    comments = sum(1 for line in lines if line.strip().startswith("#"))

    # Feature 3: Comment tatio
    # Indicates how well documented the code is
    if loc > 0:
        comment_ratio = comments / loc
    else:
        comment_ratio = 0

    # Feature 4: Number of functions
    # Use Python AST to count function definitions
    try:
        tree = ast.parse(code)

        functions = len([
            node for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ])

    except Exception:
        # If the code cannot be parsed (syntax error),
        # default to 0 functions
        functions = 0

    # Feature 5: Cyclomatic complexity
    # Measures how complicated the control flow is
    try:
        complexity = sum(c.complexity for c in cc_visit(code))
    except Exception:
        complexity = 0

    # Return the features as a list
    return [
        loc,
        comment_ratio,
        functions,
        complexity
    ]