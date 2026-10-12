from sympy import *
from simplify import *

x = symbols("x")
y = symbols("y")
str_expr = input()
expr = refactor(str_expr)
answer = sympify(expr)
print(answer)