# test_math.py
from calculator import safe_eval
import math

tests = [
    ("5", 5.0),
    ("2 * 3", 6.0),
    ("pi", math.pi),
    ("sqrt(16)", 4.0),
    ("2**3", 8.0),
    ("2^3", 8.0), # Testing my replacement of ^ with **
    ("abs(-10)", 10.0),
]

for expr, expected in tests:
    result = safe_eval(expr)
    print(f"Expr: {expr:10} | Result: {result:10} | Expected: {expected:10} | Pass: {math.isclose(result, expected)}")

# Test invalid
try:
    safe_eval("import os")
    print("Security Failure: import os allowed")
except Exception as e:
    print(f"Security Pass: import os blocked ({e})")
